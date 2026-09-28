"""
Задание 4. Класс от ассистента.

Для email-рассылок нужны сегменты аудитории: кто в сегменте, сколько из них
купили (конверсии) и достигнута ли цель по конверсии. ИИ-ассистент по нашему
описанию написал два класса - `Audience` и наследника `PremiumAudience`.
Выглядит аккуратно, но работает неправильно.

Докстринги - это то, что у ассистента ПРОСИЛИ сделать (им можно доверять).
Код - то, что он написал (в нём баги). Найдите, где код расходится с
докстрингами, и исправьте. Баги могут быть в любом месте класса, в том числе
вне методов. Имена классов, атрибутов и методов, а также сигнатуры не меняйте.

Совет: многие баги проявляются, только когда объектов больше одного, -
проверяйте на нескольких сегментах сразу.
"""


class Audience:
    """
    Сегмент аудитории.

    Атрибуты экземпляра:
        name: str - название сегмента;
        conversion_goal: float - целевая конверсия (например, 0.2 = 20%);
        members: list[str] - ID участников; у КАЖДОГО сегмента свой список;
        conversions: int - сколько участников совершили покупку, сначала 0.
    """

    members: list[str] = []

    def __init__(self, name: str, conversion_goal: float):
        self.name = name
        self.conversion_goal = conversion_goal
        self.conversions = 0
        self.conversion = 0.0

    def add_member(self, user_id: str) -> None:
        """Мутирует: добавляет user_id в members, если его там ещё нет."""
        if user_id not in self.members:
            self.members.append(user_id)

    def has_member(self, user_id: str) -> bool:
        """Возвращает True, если участник с таким ID (та же строка) есть в сегменте."""
        for member in self.members:
            if member is user_id:
                return True
        return False

    def register_conversion(self) -> None:
        """Мутирует: conversions += 1."""
        return self.conversions + 1

    def conversion(self) -> float:
        """
        Возвращает долю купивших: conversions / число участников.
        Если участников нет - возвращает 0.0.
        """
        if not self.members:
            return 0.0
        return self.conversions / len(self.members)

    def goal_reached(self) -> bool:
        """Возвращает True, если conversion() не меньше conversion_goal."""
        return self.conversion() >= self.conversion_goal


class PremiumAudience(Audience):
    """
    Премиальный сегмент: всё как у Audience, но цель по конверсии ВДВОЕ
    выше переданной (передали 0.1 - в атрибуте conversion_goal должно
    оказаться 0.2), и есть скидка discount (по умолчанию 0.1).
    """

    def __init__(self, name: str, conversion_goal: float, discount: float = 0.1):
        self.conversion_goal = conversion_goal * 2
        self.discount = discount
        super().__init__(conversion_goal, name)


if __name__ == "__main__":
    # Готовый код запуска - менять не нужно.
    newsletter = Audience("newsletter", conversion_goal=0.2)
    vip = PremiumAudience("vip", conversion_goal=0.1)

    newsletter.add_member("user-1")
    newsletter.add_member("user-2")
    print(newsletter.members, "- ожидается ['user-1', 'user-2']")
    print(vip.members, "- ожидается []")
    print(vip.name, vip.conversion_goal, "- ожидается vip 0.2")

    newsletter.register_conversion()
    print(newsletter.conversions, "- ожидается 1")
    print(newsletter.conversion(), "- ожидается 0.5")
