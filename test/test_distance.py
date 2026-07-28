from math import isclose

from src.geometry.algorithms.distance import (
    distance_point_to_segment,
)
from src.geometry.line import Line
from src.geometry.point import Point


def test_perpendicular_distance():

    line = Line(
        Point(0, 0),
        Point(10, 0),
    )

    point = Point(5, 5)

    assert isclose(
        distance_point_to_segment(point, line),
        5.0,
    )


def test_before_segment():

    line = Line(
        Point(2, 0),
        Point(8, 0),
    )

    point = Point(0, 3)

    expected = (13) ** 0.5

    assert isclose(
        distance_point_to_segment(point, line),
        expected,
    )


def test_after_segment():

    line = Line(
        Point(2, 0),
        Point(8, 0),
    )

    point = Point(10, 4)

    expected = (20) ** 0.5

    assert isclose(
        distance_point_to_segment(point, line),
        expected,
    )