"""
Задание 5. Проверка кода ассистента.

Перед отправкой восстановленного отчёта ИИ-ассистент предложил «помочь» и
написал четыре маленькие функции для финальной чистки данных. Код выглядит
аккуратно и даже запускается без ошибок - но результат у него неверный.

Докстринг каждой функции - это то, что у ассистента ПРОСИЛИ сделать (он
верный). Код под докстрингом - то, что ассистент написал (в нём баги).
Ваша задача - найти, где код расходится с докстрингом, и исправить. В
функции может быть больше одного бага. Сигнатуры не меняйте.

Совет: прежде чем править, запустите `python task5.py` и сравните вывод с
тем, что должно получиться по докстрингу.
"""


def remove_bots(user_ids: list[str], bots: set[str]) -> list[str]:
    """
    Вернуть НОВЫЙ список: user_ids без тех ID, что есть в bots. Порядок
    оставшихся ID сохраняется. Исходный список user_ids менять нельзя.

    Пример:
        remove_bots(["anna", "bot_1", "oleg"], {"bot_1"}) -> ["anna", "oleg"]
    """
    # Проходим по списку и удаляем ботов.
    for user_id in user_ids:
        if user_id in bots:
            user_ids.remove(user_id)
    return user_ids


def last_events(log_text: str, n: int) -> list[str]:
    """
    log_text - текст лога, строки разделены переводом строки.
    Вернуть последние n НЕПУСТЫХ строк лога в исходном порядке.
    Если n == 0 - вернуть пустой список. Если непустых строк меньше n -
    вернуть их все.

    Пример:
        last_events("10:00 login\\n10:05 click\\n10:07 export", 2)
        -> ["10:05 click", "10:07 export"]
    """
    # Разбиваем текст на строки и отбрасываем пустые.
    lines = []
    for line in log_text.split("/n"):
        if line:
            lines.append(line)
    # Последние n строк - срез с конца.
    return lines[-n:]


def unique_domains(emails: list[str]) -> int:
    """
    Посчитать, сколько РАЗНЫХ почтовых доменов (часть адреса после "@")
    встречается в emails. Регистр не важен: "Mail.ru" и "mail.RU" - один
    и тот же домен.

    Пример:
        unique_domains(["anna@mail.ru", "oleg@mail.ru", "ivan@gmail.com"]) -> 2
    """
    # Множество само уберёт повторы.
    domains = set()
    for email in emails:
        domains.add(email.split("@")[0])
    return len(domains)


def backoff_delays(first_delay: int, max_delay: int) -> list[int]:
    """
    Список пауз (в секундах) между повторными попытками отправить отчёт:
    первая пауза - first_delay, каждая следующая вдвое больше предыдущей.
    Вернуть все паузы, которые НЕ ПРЕВЫШАЮТ max_delay (пауза, равная
    max_delay, тоже входит). first_delay всегда больше 0.

    Пример:
        backoff_delays(1, 10) -> [1, 2, 4, 8]
    """
    delays = []
    delay = first_delay
    # Удваиваем паузу, пока не дошли до максимума.
    while delay < max_delay:
        delays.append(delay)
        delay = delay * 2
    return delays


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    users = ["anna", "bot_1", "bot_2", "oleg", "bot_3"]
    print(remove_bots(users, {"bot_1", "bot_2", "bot_3"}), "- ожидается ['anna', 'oleg']")
    print(last_events("10:00 login\n10:05 click\n\n10:07 export\n", 2), "- ожидается ['10:05 click', '10:07 export']")
    print(unique_domains(["anna@mail.ru", "oleg@mail.ru", "ivan@gmail.com"]), "- ожидается 2")
    print(backoff_delays(1, 8), "- ожидается [1, 2, 4, 8]")
