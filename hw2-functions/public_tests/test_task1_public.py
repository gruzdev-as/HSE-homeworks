from task1 import calc_cpc, calc_ctr, format_report, merge_duplicate_campaigns, parse_campaign


def test_parse_campaign_basic():
    assert parse_campaign("ADV01-001;1000;50;30.0") == {
        "campaign_id": "ADV01-001",
        "impressions": 1000,
        "clicks": 50,
        "spend": 30.0,
    }


def test_calc_ctr_basic():
    assert calc_ctr(50, 1000) == 0.05


def test_calc_cpc_basic():
    assert calc_cpc(30.0, 50) == 0.6


def test_format_report_no_duplicates():
    rows = merge_duplicate_campaigns([{"campaign_id": "a", "impressions": 1000, "clicks": 50, "spend": 30.0}])
    assert format_report(rows) == "a: CTR=5.00% CPC=0.60"
