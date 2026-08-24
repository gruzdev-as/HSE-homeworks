"""
Читает junit-xml отчёт pytest и печатает долю пройденных тестов как процент —
в лог шага и в step summary run'а. Не печатает ничего из содержимого
отдельных тестов (сообщения об ошибках, ожидаемые значения) — только
агрегированные счётчики, чтобы не спалить эталонные ответы в логах Actions.
"""

import argparse
import os
import pathlib
import sys
import xml.etree.ElementTree as ET


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("junitxml", type=pathlib.Path)
    parser.add_argument("--title", default="Оценка")
    args = parser.parse_args()

    if not args.junitxml.exists():
        print(f"::error::{args.junitxml} не найден — тесты не запустились.")
        return 1

    root = ET.parse(args.junitxml).getroot()
    suite = root if root.tag == "testsuite" else root.find(".//testsuite")
    total = int(suite.get("tests", 0))
    failed = int(suite.get("failures", 0)) + int(suite.get("errors", 0))
    skipped = int(suite.get("skipped", 0))
    passed = total - failed - skipped
    pct = 100 * passed / total if total else 0.0

    line = f"{args.title}: {pct:.1f}% ({passed}/{total} тестов пройдено)"
    print(line)

    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write(f"## {line}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
