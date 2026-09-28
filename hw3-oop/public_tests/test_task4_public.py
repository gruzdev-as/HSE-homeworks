from task4 import Audience, PremiumAudience


def test_register_conversion_basic():
    audience = Audience("newsletter", conversion_goal=0.2)
    audience.register_conversion()
    assert audience.conversions == 1


def test_premium_keeps_name():
    vip = PremiumAudience("vip", conversion_goal=0.1)
    assert vip.name == "vip"
