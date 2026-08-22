from task3 import analyze_activity


def test_analyze_basic():
    counts, unique_count, top_user = analyze_activity(["a", "b", "a", "a", "c"])
    assert counts == {"a": 3, "b": 1, "c": 1}
    assert unique_count == 3
    assert top_user == "a"
