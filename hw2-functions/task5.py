"""
Задание со звёздочкой (продвинутый трек). Декоратор-кэш.

Не входит в обязательный балл - переходите сюда, если основные 4 задания
дались легко.
"""

import functools  # noqa: F401  (пригодится для functools.wraps)


def memoize(func):
    """
    Декоратор общего назначения: кэширует результат func по позиционным
    аргументам. Повторный вызов с теми же аргументами должен вернуть
    закэшированный результат, а не вызывать func снова.

    Обёртка должна сохранять __name__ и докстринг оригинальной функции
    (см. functools.wraps) - иначе после декорирования функция "теряет"
    своё имя, что ломает отладку и интроспекцию.

    Пример:
        calls = []

        @memoize
        def slow_square(x):
            calls.append(x)
            return x * x

        slow_square(5)  # calls == [5]
        slow_square(5)  # calls всё ещё == [5] - результат взят из кэша
        slow_square(6)  # calls == [5, 6] - новый аргумент, кэша нет
    """
    # TODO: ваш код здесь
    ...


if __name__ == "__main__":
    calls = []

    @memoize
    def calc_ctr(clicks, impressions):
        calls.append((clicks, impressions))
        return clicks / impressions if impressions else 0.0

    print(calc_ctr(50, 1000))
    print(calc_ctr(50, 1000))
    print(calc_ctr(60, 2000))
    print("calls:", calls)
    print("__name__:", calc_ctr.__name__)
