# test_defects.py

from defects import log_defect, count_defects, top_defects


def test_log_defect_adds_to_log():
    log = []
    log_defect("scratch", log)
    assert log == ["scratch"]


def test_log_defect_does_not_share_default_list():
    first = log_defect("scratch")
    second = log_defect("dent")
    assert first == ["scratch"]
    assert second == ["dent"]


def test_count_defects_counts_each_type():
    log = ["scratch", "dent", "scratch"]
    assert count_defects(log) == {"scratch": 2, "dent": 1}


def test_top_defects_returns_most_common():
    log = ["scratch", "dent", "scratch", "crack", "dent", "scratch"]
    assert top_defects(log, 2) == [("scratch", 3), ("dent", 2)]
