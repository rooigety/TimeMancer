"""
This module provides functions for working with datetime objects and 
calculating time deltas.

Functions:
    time_delta(end: datetime, start: datetime) -> str:
        Calculates the time difference between two datetime objects and returns 
        a string representation of the delta.

    time_since(start: datetime) -> str:
        Returns a string representation of the time elapsed since the given 
        start datetime object.
"""

from __future__ import annotations

from datetime import datetime


def time_delta(end: datetime, start: datetime) -> str:
    """
    Calculates the time difference between two datetime objects and returns a
    string representation of the delta.

    Args:
        end (datetime): The end datetime object.
        start (datetime): The start datetime object.

    Returns:
        str: A string representation of the time delta between the two
            datetime objects.
    """
    delta = (end - start).total_seconds()

    if delta < 0.001:
        return f"{delta * 1000000:.0f}µs"
    elif delta < 1:
        return f"{delta * 1000:.3f}ms"
    elif delta < 60:
        return f"{delta:.3f}s"
    elif delta < 3600:
        return f"{delta // 60:.0f}m{delta % 60:.0f}s"
    elif delta < 86400:
        return f"{delta // 3600:.0f}h{(delta % 3600) // 60:.0f}m"
    else:
        return f"{delta // 86400:.0f}d{(delta % 86400) // 3600:.0f}h"


def time_since(start: datetime) -> str:
    """
    Returns a string representation of the time elapsed since the given start
    datetime object.

    Args:
        start (datetime): The starting datetime object.

    Returns:
        str: A string representation of the time elapsed since the given start
            datetime object.
    """
    end = datetime.now()
    return time_delta(end, start)
