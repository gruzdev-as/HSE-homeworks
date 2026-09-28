import pytest
from task3 import SpendLog


def test_add_entry_and_total_spend():
    log = SpendLog()
    log.add_entry("email", 100.0)
    log.add_entry("search", 50.0)
    assert log.total_spend() == pytest.approx(150.0)


def test_spend_by_channel_missing_channel():
    log = SpendLog()
    log.add_entry("email", 100.0)
    assert log.spend_by_channel("search") == pytest.approx(0.0)
