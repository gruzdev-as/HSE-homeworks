from task5 import last_events, unique_domains


def test_last_events_basic():
    assert last_events("10:00 login\n10:05 click\n10:07 export", 1) == ["10:07 export"]


def test_unique_domains_basic():
    assert unique_domains(["anna@mail.ru", "oleg@mail.ru"]) == 1
