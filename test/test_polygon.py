import pytest

from src.geometry.point import Point
from src.geometry.polygon import Polygon
from src.geometry.line import Line


def test_polygon_creation():

    polygon = Polygon(
        [
            Point(0, 0),
            Point(1, 0),
            Point(0, 1),
        ]
    )

    assert isinstance(
        polygon,
        Polygon,
    )


def test_polygon_requires_three_vertices():

    with pytest.raises(ValueError):

        Polygon(
            [
                Point(0, 0),
                Point(1, 1),
            ]
        )


def test_remove_last_duplicate_vertex():

    polygon = Polygon(
        [
            Point(0, 0),
            Point(1, 0),
            Point(0, 1),
            Point(0, 0),
        ]
    )

    assert len(polygon._vertices) == 3


def test_edges():

    polygon = Polygon(
        [
            Point(0,0),
            Point(4,0),
            Point(4,3),
            Point(0,3),
        ]
    )

    edges = polygon.edges()

    assert len(edges) == 4

    assert edges[0] == Line(
        Point(0,0),
        Point(4,0),
    )

    assert edges[-1] == Line(
        Point(0,3),
        Point(0,0),
    )


def test_bounding_box():

    polygon = Polygon(
        [
            Point(2, 5),
            Point(7, 4),
            Point(6, 9),
            Point(1, 8),
        ]
    )

    assert polygon.bounding_box() == (
        1,
        4,
        7,
        9,
    )


def test_contains():

    polygon = Polygon(
        [
            Point(0, 0),
            Point(10, 0),
            Point(10, 10),
            Point(0, 10),
        ]
    )

    assert polygon.contains(
        Point(5, 5)
    )

    assert not polygon.contains(
        Point(15, 5)
    )