"""
point.py

This module defines the Point class, which represents a two-dimensional point.
The Point class is the foundation of the project's geometry engine and will be
used throughout spatial algorithms such as line operations, polygons, grids,
and location recommendation.

"""

from __future__ import annotations
from math import sqrt, isclose

class Point:
    """
    Represents a point in two-dimensional space.

    Parameters
    ----------
    x : float
        X coordinate (Longitude).

    y : float
        Y coordinate (Latitude).
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def to_tuple(self) -> tuple[float, float]:
        """
        Convert the point to a tuple.

        Returns
        -------
        tuple[float, float]
            (x, y)
        """
        return self.x, self.y

    def copy(self) -> "Point":
        """
        Create a copy of this point.

        Returns
        -------
        Point
            New Point object.
        """
        return Point(self.x, self.y)

    def translate(self, dx: float, dy: float) -> None:
        """
        Move the point.

        Parameters
        ----------
        dx : float
            Offset along X.

        dy : float
            Offset along Y.
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other: "Point") -> float:
        """
        Compute Euclidean distance to another point.

        Parameters
        ----------
        other : Point

        Returns
        -------
        float
        """
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx * dx + dy * dy)

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Point):
            return False

        return (isclose(self.x, other.x) and isclose(self.y, other.y))


    def __sub__(self, other: "Point") -> tuple[float, float]:
        """
        Return the vector from another point to this point.
        Parameters
        ----------
        other : Point
        Returns
        -------
        tuple[float, float]
        (dx, dy)
        """
        return (self.x - other.x, self.y - other.y,)