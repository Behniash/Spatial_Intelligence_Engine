"""
Ray casting helper algorithms.
"""

from __future__ import annotations
from src.geometry.line import Line
from src.geometry.point import Point


def ray_intersects_segment(point: Point, segment: Line,) -> bool:
    """
    Check whether a horizontal ray extending to the right
    from the point intersects the line segment.
    """

    x1 = segment.start.x
    y1 = segment.start.y

    x2 = segment.end.x
    y2 = segment.end.y

    px = point.x
    py = point.y

    # The segment does not cross the ray's horizontal level.
    if (y1 > py) == (y2 > py):
        return False

    x_intersection = (x1 + (py - y1) * (x2 - x1) / (y2 - y1))

    return x_intersection > px