from task2 import filter_events_after

SAMPLE_LOG = [
    "10:00 alice login",
    "14:30 alice click",
    "11:15 bob login",
]


def test_filter_basic():
    assert filter_events_after(SAMPLE_LOG, "alice", "12:00") == ["14:30 alice click"]


def test_filter_no_matches():
    assert filter_events_after(SAMPLE_LOG, "carol", "00:00") == []
