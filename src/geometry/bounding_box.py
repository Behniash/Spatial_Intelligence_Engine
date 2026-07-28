"""
Bounding box geometry.
"""

from __future__ import annotations
from src.geometry.point import Point


class BoundingBox:

    def __init__(self,min_x: float, min_y: float, max_x: float, max_y: float,):
        """
        Create a rectangular bounding box.
        """

        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


    def width(self) -> float:
        """
        Return width of bounding box.
        """

        return self.max_x - self.min_x


    def height(self) -> float:
        """
        Return height of bounding box.
        """

        return self.max_y - self.min_y


    def center(self) -> Point:
        """
        Return bounding box center.
        """

        return Point(
            (self.min_x + self.max_x) / 2,
            (self.min_y + self.max_y) / 2,
        )


    def __repr__(self):
        return (
            f"BoundingBox("
            f"min_x={self.min_x}, "
            f"min_y={self.min_y}, "
            f"max_x={self.max_x}, "
            f"max_y={self.max_y})"
        )

    def contains(self, point: Point) -> bool:
        """
        Check if point is inside bounding box.
        """
        return (self.min_x <= point.x <= self.max_x and self.min_y <= point.y <= self.max_y)