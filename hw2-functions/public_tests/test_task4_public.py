from task4 import ctr_desc_then_id_asc, filter_and_sort


def test_filter_and_sort_basic():
    campaigns = [
        {"campaign_id": "a", "clicks": 0},
        {"campaign_id": "b", "clicks": 10},
    ]
    result = filter_and_sort(campaigns, predicate=lambda c: c["clicks"] > 0)
    assert result == [{"campaign_id": "b", "clicks": 10}]


def test_ctr_desc_then_id_asc_basic():
    campaigns = [
        {"campaign_id": "a", "impressions": 1000, "clicks": 10},
        {"campaign_id": "b", "impressions": 1000, "clicks": 50},
    ]
    result = sorted(campaigns, key=ctr_desc_then_id_asc)
    assert [c["campaign_id"] for c in result] == ["b", "a"]
