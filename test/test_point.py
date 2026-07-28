from src.geometry.point import Point

def test_distance():

    p1 = Point(0, 0)
    p2 = Point(3, 4)

    assert p1.distance_to(p2) == 5.0


def test_copy():

    p1 = Point(10, 20)

    p2 = p1.copy()

    assert p1 == p2

    assert p1 is not p2


def test_translate():

    p = Point(5, 7)

    p.translate(3, -2)

    assert p == Point(8, 5)