"""
Shoelace formula algorithms.

Used for polygon area and centroid calculations.
"""

from __future__ import annotations
from src.geometry.point import Point


def signed_area(vertices: list[Point]) -> float:
    """
    Calculate signed polygon area.

    Positive:
        Counter-clockwise polygon

    Negative:
        Clockwise polygon
    """

    area = 0.0

    n = len(vertices)

    for i in range(n):
        current = vertices[i]
        nxt = vertices[(i + 1) % n]

        area += current.x * nxt.y
        area -= nxt.x * current.y

    return area / 2.0


def centroid(vertices: list[Point]) -> Point:
    """
    Calculate the true centroid of a polygon.
    """

    area = signed_area(vertices)

    if area == 0:
        raise ValueError("Polygon area is zero.")

    cx = 0.0
    cy = 0.0

    n = len(vertices)

    for i in range(n):
        current = vertices[i]
        nxt = vertices[(i + 1) % n]

        cross = (
            current.x * nxt.y
            -
            nxt.x * current.y
        )

        cx += (current.x + nxt.x) * cross
        cy += (current.y + nxt.y) * cross

    cx /= 6 * area
    cy /= 6 * area

    return Point(cx, cy)