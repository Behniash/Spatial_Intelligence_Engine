"""
Douglas-Peucker polyline simplification.
"""

from __future__ import annotations

from src.geometry.line import Line
from src.geometry.point import Point
from src.geometry.algorithms.perpendicular import distance_point_to_line


def douglas_peucker(points: list[Point], epsilon: float) -> list[Point]:

    if len(points) < 3:
        return points

    start = points[0]
    end = points[-1]

    line = Line(start, end)

    max_distance = -1.0
    index = -1

    for i in range(1, len(points) - 1):

        distance = distance_point_to_line(points[i], line)

        if distance > max_distance:
            max_distance = distance
            index = i

    if max_distance <= epsilon:
        return [start, end]

    left = douglas_peucker(points[: index + 1], epsilon)
    right = douglas_peucker(points[index:], epsilon)

    return left[:-1] + right




