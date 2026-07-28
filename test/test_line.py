from src.geometry.line import Line
from src.geometry.point import Point


def test_length():

    line = Line(
        Point(0, 0),
        Point(3, 4),
    )

    assert line.length() == 5.0


def test_midpoint():

    line = Line(
        Point(0, 0),
        Point(10, 6),
    )

    assert line.midpoint() == Point(5, 3)


def test_vector():

    line = Line(
        Point(2, 1),
        Point(8, 5),
    )

    assert line.vector() == (6, 4)


def test_translate():

    line = Line(
        Point(0, 0),
        Point(2, 2),
    )

    line.translate(5, 1)

    assert line.start == Point(5, 1)

    assert line.end == Point(7, 3)


def test_copy():

    line1 = Line(
        Point(1, 2),
        Point(3, 4),
    )

    line2 = line1.copy()

    assert line1 == line2

    assert line1 is not line2