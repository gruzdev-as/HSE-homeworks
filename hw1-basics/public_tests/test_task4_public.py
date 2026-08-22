import pytest
from task4 import average_ctr


def test_average_ctr_basic():
    records = [
        {"ad_id": "a1", "impressions": 100, "clicks": 10},
        {"ad_id": "a2", "impressions": 200, "clicks": 20},
    ]
    assert average_ctr(records) == pytest.approx(0.1)
