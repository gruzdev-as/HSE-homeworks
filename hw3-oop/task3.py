"""
Задание 3. Рефакторинг procedural_code.py в класс SpendLog по диаграмме
diagrams/task3_spendlog.txt.
"""


class SpendLog:
    def __init__(self):
        # TODO: ваш код здесь
        ...

    def add_entry(self, channel: str, amount: float) -> None:
        """Мутирует: добавляет запись {"channel": channel, "amount": amount} в entries."""
        # TODO: ваш код здесь
        ...

    def total_spend(self) -> float:
        """Возвращает сумму amount по всем записям."""
        # TODO: ваш код здесь
        ...

    def spend_by_channel(self, channel: str) -> float:
        """Возвращает сумму amount по записям с данным channel; 0.0, если такого channel нет."""
        # TODO: ваш код здесь
        ...

    def summary(self) -> str:
        """
        Возвращает многострочный отчёт: для каждого канала (по алфавиту)
        строка "{channel}: {сумма:.2f}", последней строкой -
        "Итого: {общая сумма:.2f}".
        """
        # TODO: ваш код здесь
        ...


if __name__ == "__main__":
    log = SpendLog()
    log.add_entry("email", 120.50)
    log.add_entry("search", 300.00)
    log.add_entry("email", 45.25)
    print(log.summary())
