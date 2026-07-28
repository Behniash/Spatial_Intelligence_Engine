"""
perpendicular.py

Perpendicular distance algorithms.
"""

from __future__ import annotations

from math import sqrt

from src.geometry.line import Line
from src.geometry.point import Point


def distance_point_to_line(point: Point, line: Line) -> float:
    """
    Compute the perpendicular distance between a point
    and an infinite line.
    """

    ax = line.start.x
    ay = line.start.y

    bx = line.end.x
    by = line.end.y

    px = point.x
    py = point.y

    dx = bx - ax
    dy = by - ay

    denominator = sqrt(dx * dx + dy * dy)

    if denominator == 0:
        raise ValueError("Line length cannot be zero.")

    numerator = abs(dx * (ay - py) -(ax - px) * dy)

    return numerator / denominator