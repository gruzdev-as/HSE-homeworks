"""
Задание 1. Рефакторинг отчёта по кампаниям.

Скрипт ИИ-ассистента (messy_code.py) считает то же самое, но написан плохо и
содержит баги. Ваша задача - реализовать те же вычисления как отдельные
функции с чёткими контрактами и БЕЗ багов оригинала. Посмотрите
messy_code.py и запустите его (`python messy_code.py`), прежде чем начинать -
там видно, что именно идёт не так.
"""


def parse_campaign(line: str) -> dict:
    """
    line - строка вида "CID-001;15320;412;530.40"
    (campaign_id;impressions;clicks;spend), поля разделены `;`.

    Вернуть {"campaign_id": str, "impressions": int, "clicks": int, "spend": float}.

    Пример:
        parse_campaign("ADV01-001;1000;50;30.0")
        -> {"campaign_id": "ADV01-001", "impressions": 1000, "clicks": 50, "spend": 30.0}
    """
    # TODO: ваш код здесь
    ...


def calc_ctr(clicks: int, impressions: int) -> float:
    """
    CTR = clicks / impressions.

    Если impressions <= 0 - вернуть 0.0 (а не бросать исключение и не
    округлять до целого).

    Пример:
        calc_ctr(50, 1000) -> 0.05
        calc_ctr(0, 0) -> 0.0
    """
    # TODO: ваш код здесь
    ...


def calc_cpc(spend: float, clicks: int) -> float:
    """
    CPC = spend / clicks.

    Если clicks <= 0 - вернуть 0.0 (а не бросать исключение).

    Пример:
        calc_cpc(30.0, 50) -> 0.6
        calc_cpc(75.0, 0) -> 0.0
    """
    # TODO: ваш код здесь
    ...


def merge_duplicate_campaigns(records: list[dict]) -> list[dict]:
    """
    records - список словарей вида
    {"campaign_id": str, "impressions": int, "clicks": int, "spend": float},
    возможно с повторяющимися campaign_id (экспортёр иногда выгружает одну
    кампанию дважды).

    Для каждого повторяющегося campaign_id сложить impressions, clicks и
    spend в одну запись. Порядок записей в результате - по первому
    появлению campaign_id в records.

    Исходный список records и словари в нём менять нельзя: вернуть новые
    словари, а не дописывать суммы в записи из records.

    Пример:
        merge_duplicate_campaigns([
            {"campaign_id": "a", "impressions": 100, "clicks": 10, "spend": 5.0},
            {"campaign_id": "b", "impressions": 200, "clicks": 20, "spend": 8.0},
            {"campaign_id": "a", "impressions": 50, "clicks": 5, "spend": 2.0},
        ])
        -> [
            {"campaign_id": "a", "impressions": 150, "clicks": 15, "spend": 7.0},
            {"campaign_id": "b", "impressions": 200, "clicks": 20, "spend": 8.0},
        ]
    """
    # TODO: ваш код здесь
    ...


def format_report(rows: list[dict]) -> str:
    """
    rows - список словарей вида
    {"campaign_id": str, "impressions": int, "clicks": int, "spend": float}
    (уже без дублей - предполагается, что merge_duplicate_campaigns вызван
    раньше).

    Вернуть многострочный отчёт: по одной строке на кампанию, в том же
    порядке, что и в rows, в формате
    "{campaign_id}: CTR={ctr:.2%} CPC={cpc:.2f}", используя calc_ctr и
    calc_cpc.

    Пример:
        format_report([{"campaign_id": "a", "impressions": 1000, "clicks": 50, "spend": 30.0}])
        -> "a: CTR=5.00% CPC=0.60"
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    with open("data/campaigns_sample.txt", encoding="utf-8") as f:
        records = [parse_campaign(line) for line in f if line.strip()]

    merged = merge_duplicate_campaigns(records)
    print(format_report(merged))
