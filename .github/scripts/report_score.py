"""
Читает junit-xml отчёт pytest и печатает оценку - долю пройденных тестов
от 0 до 1 с округлением до сотых (например, 0.83) - в лог шага и в step
summary run'а. С --json дополнительно пишет её в файл, который workflow
выгружает артефактом: так оценки потом можно собрать автоматически.

Не печатает ничего из содержимого отдельных тестов (сообщения об ошибках,
ожидаемые значения) - только агрегированные счётчики, чтобы не спалить
эталонные ответы в логах Actions.
"""

import argparse
import json
import os
import pathlib
import sys
import xml.etree.ElementTree as ET


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("junitxml", type=pathlib.Path)
    parser.add_argument("--title", default="Оценка")
    parser.add_argument("--json", type=pathlib.Path, help="куда записать оценку в машиночитаемом виде")
    args = parser.parse_args()

    if not args.junitxml.exists():
        print(f"::error::{args.junitxml} не найден - тесты не запустились.")
        return 1

    root = ET.parse(args.junitxml).getroot()
    suite = root if root.tag == "testsuite" else root.find(".//testsuite")
    total = int(suite.get("tests", 0))
    failed = int(suite.get("failures", 0)) + int(suite.get("errors", 0))
    skipped = int(suite.get("skipped", 0))
    passed = total - failed - skipped
    score = round(passed / total, 2) if total else 0.0

    line = f"{args.title}: {score:.2f}"
    details = f"пройдено тестов: {passed} из {total}"
    print(f"{line} ({details})")

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(f"## {line}\n{details}\n\n")

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "title": args.title,
            "score": score,
            "passed": passed,
            "total": total,
            "commit": os.environ.get("GITHUB_SHA", ""),
        }
        args.json.write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    sys.exit(main())
