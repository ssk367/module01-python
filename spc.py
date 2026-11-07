# spc.py
import statistics

D2 = 1.128


def individual_limits(readings: list[float]) -> tuple[float, float, float]:
    """Calculate individual control limits for a set of readings.

    Args:
        readings (list[float]): A list of individual measurements.

    Returns:
        tuple[float, float, float]: A tuple containing the lower control limit, mean, and upper control limit.
    """

    if len(readings) < 2:
        raise ValueError(
            "The readings list must contain at least two measurements to calculate a moving range."
        )

    moving_ranges = [abs(a - b) for a, b in zip(readings, readings[1:])]
    average_mr = statistics.mean(moving_ranges)
    sigma = average_mr / D2
    mean = statistics.mean(readings)
    lcl = mean - 3 * sigma
    ucl = mean + 3 * sigma

    return lcl, mean, ucl
