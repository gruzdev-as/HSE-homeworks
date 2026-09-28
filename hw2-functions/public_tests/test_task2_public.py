from task2 import unique_advertisers


def test_unique_advertisers_basic():
    assert unique_advertisers(["ADV07-014", "ADV01-002", "ADV07-015"]) == ["ADV07", "ADV01"]


def test_unique_advertisers_empty():
    assert unique_advertisers([]) == []
