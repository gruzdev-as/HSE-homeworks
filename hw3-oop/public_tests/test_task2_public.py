import pytest
from task2 import AdChannel, EmailChannel, SearchChannel


def test_base_cost_per_click():
    channel = AdChannel("Generic", budget=100.0)
    channel.register_click()
    channel.register_click()
    assert channel.cost_per_click() == pytest.approx(50.0)


def test_subclass_keeps_base_attrs():
    channel = SearchChannel("Google Ads", budget=200.0)
    assert channel.name == "Google Ads"
    assert channel.budget == 200.0


def test_email_channel_applies_floor():
    channel = EmailChannel("Newsletter", budget=0.01, min_cost_per_click=0.05)
    channel.register_click()
    assert channel.cost_per_click() == pytest.approx(0.05)
