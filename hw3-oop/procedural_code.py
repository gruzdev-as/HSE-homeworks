"""
Процедурный трекер расходов по каналам одной кампании: данные (список
записей) и поведение (функции) существуют отдельно друг от друга. Работает
без ошибок, но задание 3 просит переписать это как класс.
"""


def add_entry(log: list[dict], channel: str, amount: float) -> list[dict]:
    """Добавить запись {"channel": channel, "amount": amount} в log и вернуть log."""
    log.append({"channel": channel, "amount": amount})
    return log


def total_spend(log: list[dict]) -> float:
    """Сумма amount по всем записям log."""
    return sum(entry["amount"] for entry in log)


def spend_by_channel(log: list[dict], channel: str) -> float:
    """Сумма amount по записям с данным channel; 0.0, если такого channel нет."""
    return sum(entry["amount"] for entry in log if entry["channel"] == channel)


def format_summary(log: list[dict]) -> str:
    """Многострочная сводка: по каждому каналу - сумма, последней строкой - общий итог."""
    channels = sorted({entry["channel"] for entry in log})
    lines = [f"{channel}: {spend_by_channel(log, channel):.2f}" for channel in channels]
    lines.append(f"Итого: {total_spend(log):.2f}")
    return "\n".join(lines)


if __name__ == "__main__":
    log: list[dict] = []
    add_entry(log, "email", 120.50)
    add_entry(log, "search", 300.00)
    add_entry(log, "email", 45.25)
    print(format_summary(log))
