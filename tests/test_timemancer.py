from datetime import datetime, timedelta

import pytest

import timemancer as tm


@pytest.fixture
def now():
    return datetime.now()


@pytest.mark.parametrize(
    "delta, expected",
    [
        (timedelta(days=1, hours=3, minutes=34), "1d3h"),
        (timedelta(days=1, hours=3), "1d3h"),
        (timedelta(minutes=220), "3h40m"),
        (timedelta(minutes=60), "1h0m"),
        (timedelta(minutes=59), "59m0s"),
        (timedelta(seconds=83), "1m23s"),
    ],
    ids=["day-hour1", "day-hour2", "hour-minute", "one-hour", "minute", "min-sec"],
)
def test_time_since(now, delta, expected):
    # Arrange.
    dt = now - delta

    # Act.
    result = tm.time_since(dt)

    # Assert.
    assert result == expected
