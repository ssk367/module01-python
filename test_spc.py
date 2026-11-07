# test_spc.py
import pytest

from spc import individual_limits


def test_individual_limits_use_moving_range():
    readings = [10.3, 12.1, 11.6, 13.3, 12.0]
    lcl, mean, ucl = individual_limits(readings)
    assert lcl == pytest.approx(8.34, abs=0.01)
    assert mean == pytest.approx(11.86, abs=0.01)
    assert ucl == pytest.approx(15.38, abs=0.01)


@pytest.mark.parametrize("readings", [[], [10.3]], ids=["empty", "one_reading"])
def test_individual_limits_raises_for_insufficient_readings(readings):
    with pytest.raises(
        ValueError,
        match="at least two measurements",
    ):
        individual_limits(readings)
