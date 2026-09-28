"""
Задание 1. Класс Campaign по диаграмме diagrams/task1_campaign.txt.
"""


class Campaign:
    def __init__(self, name: str, budget: float):
        # TODO: ваш код здесь
        ...

    def register_impression(self) -> None:
        """Мутирует: impressions += 1."""
        # TODO: ваш код здесь
        ...

    def register_click(self) -> None:
        """Мутирует: clicks += 1."""
        # TODO: ваш код здесь
        ...

    def ctr(self) -> float:
        """
        Возвращает CTR в процентах (clicks / impressions * 100), ничего не
        сохраняет. Если impressions == 0 - возвращает 0.0.
        """
        # TODO: ваш код здесь
        ...

    def spend_amount(self, amount: float) -> None:
        """Мутирует: spend += amount."""
        # TODO: ваш код здесь
        ...

    def is_active(self) -> bool:
        """
        Возвращает spend < budget. Вычисляется заново при КАЖДОМ вызове -
        не кешируйте результат в отдельном атрибуте.
        """
        # TODO: ваш код здесь
        ...


if __name__ == "__main__":
    campaign = Campaign("Search", budget=1000.0)
    campaign.register_impression()
    campaign.register_impression()
    campaign.register_click()
    campaign.spend_amount(50.0)
    print(campaign.ctr())
    print(campaign.is_active())
