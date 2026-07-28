"""
distance.py

Distance-related algorithms for the geometry engine.
"""

from __future__ import annotations

from math import sqrt

from src.geometry.line import Line
from src.geometry.point import Point


def distance_point_to_segment(point: Point, line: Line,) -> float:
    """
    Compute the shortest Euclidean distance between a point
    and a line segment.

    Parameters
    ----------
    point : Point

    line : Line

    Returns
    -------
    float
    """

    ax = line.start.x
    ay = line.start.y

    bx = line.end.x
    by = line.end.y

    px = point.x
    py = point.y

    abx = bx - ax
    aby = by - ay

    apx = px - ax
    apy = py - ay

    ab_squared = abx * abx + aby * aby

    # Projection factor
    t = (apx * abx + apy * aby) / ab_squared

    # Closest point is A
    if t <= 0:
        closest_x = ax
        closest_y = ay

    # Closest point is B
    elif t >= 1:
        closest_x = bx
        closest_y = by

    # Closest point lies on segment
    else:
        closest_x = ax + t * abx
        closest_y = ay + t * aby

    dx = px - closest_x
    dy = py - closest_y

    return sqrt(dx * dx + dy * dy)