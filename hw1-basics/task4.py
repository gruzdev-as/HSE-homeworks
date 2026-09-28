"""
Задание 4. Валидация CTR.

Следующий шаг - посчитать средний CTR по рекламным объявлениям. Часть
записей в выгрузке повреждена ИИ-ассистентом и должна быть исключена из
расчёта.
"""


def average_ctr(records: list[dict]) -> float:
    """
    records - список словарей вида
    {"ad_id": str, "impressions": int, "clicks": int}.

    Для каждой ЧИСТОЙ записи посчитать CTR = clicks / impressions и вернуть
    среднее арифметическое CTR по всем чистым записям (не взвешенное по
    показам).

    Запись считается «грязной» и должна быть исключена из расчёта, если
    выполняется хотя бы одно из условий:
      - impressions <= 0;
      - clicks < 0;
      - clicks > impressions.

    Если чистых записей не осталось вообще, вернуть 0.0.

    Пример:
        average_ctr([{"ad_id": "a", "impressions": 100, "clicks": 10}])
        -> 0.1
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    import csv

    with open("data/task4_ads.csv", encoding="utf-8", newline="") as f:
        records = [
            {
                "ad_id": row["ad_id"],
                "impressions": int(row["impressions"]),
                "clicks": int(row["clicks"]),
            }
            for row in csv.DictReader(f)
        ]

    print(average_ctr(records))
