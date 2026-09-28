"""
Это не задание - это улика. Скрипт, которым ИИ-ассистент генерировал отчёты
по рекламным кампаниям. Он «работает» (иногда), но:

  - всё в одной функции, без разбиения на смысловые шаги;
  - дублирует код форматирования (для консоли и для «файла»);
  - содержит минимум два бага, которые тихо портят отчёт (а один - роняет
    программу совсем).

Прежде чем чинить код в task1.py, запустите этот файл на данных из data/ и
посмотрите сами, что не так:

    python messy_code.py

Трогать этот файл не нужно - задание 1 просит написать ЧИСТУЮ версию в
task1.py, а не исправить этот.
"""


def generate_campaign_report(path):
    report_lines_console = []
    report_lines_file = []

    with open(path, encoding="utf-8") as f:
        for raw_line in f:
            raw_line = raw_line.strip()
            if not raw_line:
                continue
            # Баг 1: если campaign_id уже встречался выше (экспортёр выгрузил
            # кампанию два раза), строка просто добавляется в отчёт ещё раз -
            # вместо того, чтобы сложить показатели в одну запись. Отчёт
            # получается раздутым: одна кампания посчитана как две.
            parts = raw_line.split(";")
            campaign_id = parts[0]
            impressions = int(parts[1])
            clicks = int(parts[2])
            spend = float(parts[3])

            # Баг 2: целочисленное деление вместо обычного - CTR почти всегда
            # округляется до 0.
            ctr = clicks // impressions
            # Баг 3: деление на clicks без проверки на 0 - падает, если у
            # кампании 0 кликов.
            cpc = spend / clicks

            console_line = "campaign " + campaign_id + " ctr=" + str(ctr) + " cpc=" + str(round(cpc, 2))
            report_lines_console.append(console_line)

            file_line = campaign_id + "," + str(ctr) + "," + str(round(cpc, 2))
            report_lines_file.append(file_line)

    for line in report_lines_console:
        print(line)

    return report_lines_file


if __name__ == "__main__":
    generate_campaign_report("data/campaigns_sample.txt")
