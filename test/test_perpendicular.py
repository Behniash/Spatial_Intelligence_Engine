from math import isclose

from src.geometry.algorithms.perpendicular import distance_point_to_line
from src.geometry.line import Line
from src.geometry.point import Point


def test_horizontal_line():

    line = Line(Point(0, 0), Point(10, 0))

    point = Point(5, 5)

    assert isclose(distance_point_to_line(point, line), 5.0,)


def test_vertical_line():

    line = Line(Point(3, 0), Point(3, 10))

    point = Point(8, 5)

    assert isclose(distance_point_to_line(point, line), 5.0,)


def test_point_on_line():

    line = Line(Point(0, 0), Point(10, 10))

    point = Point(5, 5)

    assert isclose(distance_point_to_line(point, line), 0.0,)