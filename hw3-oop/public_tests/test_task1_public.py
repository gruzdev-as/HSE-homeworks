import pytest
from task1 import Campaign


def test_ctr_basic():
    campaign = Campaign("Search", budget=1000.0)
    campaign.register_impression()
    campaign.register_impression()
    campaign.register_click()
    assert campaign.ctr() == pytest.approx(50.0)


def test_is_active_basic():
    campaign = Campaign("Search", budget=100.0)
    assert campaign.is_active() is True
    campaign.spend_amount(150.0)
    assert campaign.is_active() is False
