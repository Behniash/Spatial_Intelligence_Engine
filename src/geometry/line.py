"""
line.py

Defines the Line class used throughout the geometry engine.

A Line represents a line segment defined by two Point objects.

"""

from __future__ import annotations
from src.geometry.point import Point


class Line:
    """
    Represents a line segment between two points.

    Parameters
    ----------
    start : Point
        Starting point.

    end : Point
        Ending point.
    """

    def __init__(self, start: Point, end: Point) -> None:

        if start == end:
            raise ValueError(
                "A line segment requires two distinct points."
            )

        self.start = start.copy()
        self.end = end.copy()

    def length(self) -> float:
        """
        Compute the Euclidean length of the line segment.

        Returns
        -------
        float
            Length of the line.
        """
        return self.start.distance_to(self.end)

    def midpoint(self) -> Point:
        """
        Compute the midpoint of the line segment.

        Returns
        -------
        Point
            Midpoint.
        """

        return Point(
            (self.start.x + self.end.x) / 2,
            (self.start.y + self.end.y) / 2,
        )

    def vector(self) -> tuple[float, float]:
        """
        Return the vector from start to end.

        Returns
        -------
        tuple[float, float]
            (dx, dy)
        """

        return self.end - self.start

    def translate(self, dx: float, dy: float,) -> None:
        """
        Translate the line.

        Parameters
        ----------
        dx : float

        dy : float
        """

        self.start.translate(dx, dy)
        self.end.translate(dx, dy)

    def copy(self) -> "Line":
        """
        Return a copy of the line.
        """

        return Line(self.start, self.end,)

    def __repr__(self) -> str:

        return (f"Line(start={self.start}, " f"end={self.end})")

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Line):
            return False

        return (self.start == other.start and self.end == other.end)