"""
Читает junit-xml отчёт pytest и печатает оценку от 0 до 1 с округлением до
сотых (например, 0.83) - в лог шага и в step summary run'а. С --json
дополнительно пишет её в файл, который workflow выгружает артефактом: так
оценки потом можно собрать автоматически.

Все задания весят одинаково: для каждого задания из --tasks считается доля
пройденных тестов, а оценка - среднее этих долей. Иначе задание с 15 тестами
весило бы втрое больше задания с 5. Задание, файл которого не импортируется
(синтаксическая ошибка, переименованная функция), получает 0, но остальные
задания считаются как обычно - для этого pytest запускается с
--continue-on-collection-errors.

Не печатает ничего из содержимого отдельных тестов (имена, сообщения об
ошибках, ожидаемые значения) - только счётчики по заданиям, чтобы не спалить
эталонные ответы в логах Actions.
"""

import argparse
import json
import os
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

# test_task1_public.py, test_task1_hidden.py, test_task_bonus_hidden.py -> task1 / task_bonus
TASK_OF_MODULE = re.compile(r"test_(task\w+?)_(?:public|hidden)\b")


def task_of(case: ET.Element) -> str | None:
    # У обычного теста модуль лежит в classname, у ошибки сбора (файл не импортируется) - в name.
    match = TASK_OF_MODULE.search(case.get("classname") or "") or TASK_OF_MODULE.search(case.get("name") or "")
    return match.group(1) if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("junitxml", type=pathlib.Path)
    parser.add_argument("--tasks", required=True, help="задания через запятую, например task1,task2,task3")
    parser.add_argument("--title", default="Оценка")
    parser.add_argument("--json", type=pathlib.Path, help="куда записать оценку в машиночитаемом виде")
    args = parser.parse_args()
    tasks = [t.strip() for t in args.tasks.split(",") if t.strip()]

    if not args.junitxml.exists():
        print(f"::error::{args.junitxml} не найден - тесты не запустились.")
        return 1

    counts = {task: {"passed": 0, "total": 0} for task in tasks}
    not_importable = set()
    for case in ET.parse(args.junitxml).getroot().iter("testcase"):
        task = task_of(case)
        if task not in counts:
            continue
        counts[task]["total"] += 1
        if not any(child.tag in ("failure", "error", "skipped") for child in case):
            counts[task]["passed"] += 1
        # Ошибка сбора тестов (у такой записи нет classname): файл задания не импортируется.
        if not case.get("classname") and any(child.tag == "error" for child in case):
            not_importable.add(task)

    task_scores = {t: c["passed"] / c["total"] if c["total"] else 0.0 for t, c in counts.items()}
    score = round(sum(task_scores.values()) / len(tasks), 2) if tasks else 0.0

    line = f"{args.title}: {score:.2f}"
    details = []
    for t, c in counts.items():
        line_t = f"{t}: пройдено {c['passed']} из {c['total']}"
        if t in not_importable:
            line_t += f" - файл {t}.py не запускается, выполните `python {t}.py` локально и посмотрите ошибку"
        details.append(line_t)
    print(line)
    for d in details:
        print(f"  {d}")

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(f"## {line}\n")
            f.write("Все задания весят одинаково: оценка - среднее по заданиям.\n\n")
            f.write("".join(f"- {d}\n" for d in details) + "\n")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "title": args.title,
            "score": score,
            "tasks": {t: {**c, "score": round(task_scores[t], 2)} for t, c in counts.items()},
            "commit": os.environ.get("GITHUB_SHA", ""),
        }
        args.json.write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
