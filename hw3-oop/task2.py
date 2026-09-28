"""
Задание 2. Иерархия AdChannel по диаграмме diagrams/task2_channels.txt.
"""


class AdChannel:
    def __init__(self, name: str, budget: float):
        # TODO: ваш код здесь
        ...

    def register_click(self) -> None:
        """Мутирует: clicks += 1."""
        # TODO: ваш код здесь
        ...

    def cost_per_click(self) -> float:
        """Возвращает budget / clicks. Если clicks == 0 - возвращает 0.0."""
        # TODO: ваш код здесь
        ...


class EmailChannel(AdChannel):
    def __init__(self, name: str, budget: float, min_cost_per_click: float = 0.05):
        # TODO: ваш код здесь (не забудьте super().__init__(name, budget))
        ...

    def cost_per_click(self) -> float:
        """Переопределяет: max(cost_per_click() базового класса, min_cost_per_click)."""
        # TODO: ваш код здесь
        ...


class SocialChannel(AdChannel):
    def __init__(self, name: str, budget: float, platform_fee: float = 0.10):
        # TODO: ваш код здесь (не забудьте super().__init__(name, budget))
        ...

    def cost_per_click(self) -> float:
        """Переопределяет: cost_per_click() базового класса + platform_fee."""
        # TODO: ваш код здесь
        ...


class SearchChannel(AdChannel):
    def __init__(self, name: str, budget: float, bid_multiplier: float = 1.2):
        # TODO: ваш код здесь (не забудьте super().__init__(name, budget))
        ...

    def cost_per_click(self) -> float:
        """Переопределяет: cost_per_click() базового класса * bid_multiplier."""
        # TODO: ваш код здесь
        ...


if __name__ == "__main__":
    channels = [
        EmailChannel("Newsletter", budget=100.0),
        SocialChannel("Instagram", budget=500.0),
        SearchChannel("Google Ads", budget=800.0),
    ]
    for channel in channels:
        channel.register_click()
        channel.register_click()
        print(channel.name, channel.cost_per_click())
