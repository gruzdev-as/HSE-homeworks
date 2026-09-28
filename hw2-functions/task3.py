"""
Задание 3. Объединение отчётов (*args) и лог предупреждений с тегами (**kwargs).
"""


def aggregate_campaigns(*reports: list[dict], sort_by: str = "ctr", reverse: bool = True) -> list[dict]:
    """
    reports - произвольное число списков словарей кампаний вида
    {"campaign_id": str, "impressions": int, "clicks": int, "spend": float}
    (например, отчёты за разные дни).

    Объединить все записи из всех reports в один список. Для каждой записи
    досчитать и добавить ключи "ctr" (clicks / impressions, 0.0 если
    impressions == 0) и "cpc" (spend / clicks, 0.0 если clicks == 0).
    Ключи добавляются в НОВЫЕ словари-копии: исходные отчёты после вызова
    должны остаться такими же, как были.

    Отсортировать результат по полю sort_by (например, "ctr", "cpc",
    "impressions", "clicks", "spend"); reverse управляет направлением
    сортировки (по умолчанию - по убыванию).

    Пример:
        aggregate_campaigns(
            [{"campaign_id": "a", "impressions": 1000, "clicks": 50, "spend": 30.0}],
            [{"campaign_id": "b", "impressions": 2000, "clicks": 60, "spend": 40.0}],
            sort_by="ctr",
        )
        -> [{..., "campaign_id": "a", "ctr": 0.05, ...}, {..., "campaign_id": "b", "ctr": 0.03, ...}]
    """
    # TODO: ваш код здесь
    ...


def log_alert(campaign_id: str, message: str, log: list[str] | None = None, **tags) -> list[str]:
    """
    Добавить строку "{campaign_id}: {message}" в log и вернуть log.

    Если log не передан - начать НОВЫЙ список (а не переиспользовать один и
    тот же список между разными вызовами функции).

    tags - любые дополнительные именованные аргументы (например,
    severity="high", channel="email"). Если они переданы, в конец строки
    дописывается " [имя=значение, имя=значение]", причём теги идут по
    алфавиту имён - в каком бы порядке их ни передали. Значения могут быть
    любого типа (например, числа). Если тегов нет - квадратных скобок в
    строке нет вообще.

    Пример:
        log_alert("a", "budget overrun") -> ["a: budget overrun"]
        log_alert("b", "low ctr", log=["a: budget overrun"])
        -> ["a: budget overrun", "b: low ctr"]
        log_alert("c", "spend spike", severity="high", channel="email")
        -> ["c: spend spike [channel=email, severity=high]"]
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    day1 = [{"campaign_id": "a", "impressions": 1000, "clicks": 50, "spend": 30.0}]
    day2 = [{"campaign_id": "b", "impressions": 2000, "clicks": 60, "spend": 40.0}]
    print(aggregate_campaigns(day1, day2))
    print(log_alert("a", "budget overrun"))
    print(log_alert("c", "spend spike", severity="high", channel="email"))
