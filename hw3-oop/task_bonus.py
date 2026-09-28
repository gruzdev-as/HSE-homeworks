"""
Бонус (продвинутый трек), диаграмма diagrams/task_bonus_composition.txt.

Часть 1: добавьте __repr__ и __eq__ прямо в класс Campaign в task1.py -
здесь их писать не нужно, скрытые тесты бонуса импортируют Campaign
из task1 и проверяют эти методы там.

Часть 2: класс CampaignWithChannels ниже - композиция вместо наследования.
"""

from task1 import Campaign
from task2 import AdChannel


class CampaignWithChannels:
    def __init__(self, campaign: Campaign):
        # TODO: ваш код здесь
        ...

    def add_channel(self, channel: AdChannel) -> None:
        """Мутирует: добавляет channel в channels."""
        # TODO: ваш код здесь
        ...

    def total_cost(self) -> float:
        """
        Возвращает сумму cost_per_click() * clicks по всем channels -
        делегируйте расчёт каналам, не пересчитывайте вручную.
        """
        # TODO: ваш код здесь
        ...

    def __repr__(self) -> str:
        # TODO: ваш код здесь
        ...

    def __eq__(self, other) -> bool:
        """Равны, если равны campaign (через его __eq__) и совпадают списки channels."""
        # TODO: ваш код здесь
        ...


if __name__ == "__main__":
    from task2 import EmailChannel, SearchChannel

    campaign = Campaign("Search", budget=1000.0)
    bundle = CampaignWithChannels(campaign)

    newsletter = EmailChannel("Newsletter", budget=100.0)
    newsletter.register_click()
    bundle.add_channel(newsletter)

    google_ads = SearchChannel("Google Ads", budget=800.0)
    google_ads.register_click()
    bundle.add_channel(google_ads)

    print(bundle.total_cost())
