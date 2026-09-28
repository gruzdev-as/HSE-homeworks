from task3 import aggregate_campaigns, log_alert


def test_aggregate_campaigns_basic():
    day1 = [{"campaign_id": "a", "impressions": 1000, "clicks": 50, "spend": 30.0}]
    day2 = [{"campaign_id": "b", "impressions": 2000, "clicks": 60, "spend": 40.0}]
    result = aggregate_campaigns(day1, day2, sort_by="ctr", reverse=True)
    assert [row["campaign_id"] for row in result] == ["a", "b"]


def test_log_alert_basic():
    assert log_alert("a", "budget overrun") == ["a: budget overrun"]


def test_log_alert_with_one_tag():
    assert log_alert("a", "low ctr", severity="high") == ["a: low ctr [severity=high]"]
