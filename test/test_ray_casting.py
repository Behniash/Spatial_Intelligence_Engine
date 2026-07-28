from src.geometry.algorithms.ray_casting import (
    ray_intersects_segment,
)
from src.geometry.line import Line
from src.geometry.point import Point


def test_ray_intersects():

    segment = Line(
        Point(5, 0),
        Point(5, 10),
    )

    point = Point(2, 5)

    assert ray_intersects_segment(
        point,
        segment,
    )


def test_ray_does_not_intersect():

    segment = Line(
        Point(5, 0),
        Point(5, 10),
    )

    point = Point(7, 5)

    assert not ray_intersects_segment(
        point,
        segment,
    )