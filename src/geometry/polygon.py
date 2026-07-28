"""
polygon.py

Defines the Polygon class used throughout the geometry engine.

A polygon is represented as an ordered collection of vertices.

"""

from __future__ import annotations
from src.geometry.point import Point
from src.geometry.line import Line
from src.geometry.algorithms.ray_casting import (ray_intersects_segment,)
from src.geometry.algorithms.douglas_peucker import douglas_peucker
from src.geometry.algorithms.shoelace import signed_area, centroid
from src.geometry.bounding_box import BoundingBox

class Polygon:
    """
    Represents a simple polygon.

    Parameters
    ----------
    vertices : list[Point]
        Ordered polygon vertices.
    """

    def __init__(self, vertices: list[Point],) -> None:

        if len(vertices) < 3:
            raise ValueError("A polygon requires at least three vertices.")

        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError("All vertices must be Point objects.")

        # GeoJSON polygons repeat the first vertex at the end.
        # Internally we keep only unique vertices.
        if vertices[0] == vertices[-1]:
            vertices = vertices[:-1]

        if len(vertices) < 3:
            raise ValueError("A polygon requires at least three unique vertices.")

        self._vertices = [vertex.copy() for vertex in vertices]


    @property
    def vertices(self) -> tuple[Point, ...]:
        """
        Return a read-only copy of polygon vertices.

        Returns
        -------
        tuple[Point, ...]
        Polygon vertices.
        """
        return tuple(vertex.copy() for vertex in self._vertices)


    def __len__(self) -> int:
        """
        Return the number of polygon vertices.
        """
        return len(self._vertices)


    def copy(self) -> "Polygon":
        """
        Return a copy of the polygon.
        """
        return Polygon(self._vertices)


    def edges(self) -> list[Line]:
        """
        Return all polygon edges.

        Returns
        -------
        list[Line]
            Polygon edges.
        """
        edges = []

        n = len(self._vertices)

        for i in range(n):
            start = self._vertices[i]
            end = self._vertices[(i + 1) % n]
            edges.append(Line(start, end,))

        return edges


    def bounding_box(self) -> tuple[float, float, float, float]:
        """
        Compute the polygon bounding box.
        Returns
        -------
        tuple[float, float, float, float]
            (min_x, min_y, max_x, max_y)
        """
        xs = [vertex.x for vertex in self._vertices]
        ys = [vertex.y for vertex in self._vertices]

        return (min(xs), min(ys), max(xs), max(ys),)


    def __repr__(self) -> str:
        return (f"Polygon("f"vertices={len(self)}"f")")


    def contains(self,point: Point,) -> bool:
        """
        Check whether a point lies inside the polygon
        using the Ray Casting algorithm.
        Parameters
        ----------
        point : Point
        Returns
        -------
        bool
        """
        intersections = 0
        for edge in self.edges():
            if ray_intersects_segment(point, edge,):
                intersections += 1
        return intersections % 2 == 1


    def __len__(self):
        return len(self._vertices)


    def __getitem__(self, index):
        return self._vertices[index]


    def __iter__(self):
        return iter(self._vertices)


    def simplify(self, epsilon: float) -> "Polygon":
        """
        Return a simplified copy of the polygon.
        """
        simplified = douglas_peucker(self._vertices, epsilon)
        return Polygon(simplified)


    def area(self) -> float:
        return abs(signed_area(self._vertices))


    def perimeter(self) -> float:
        """
        Compute the perimeter of the polygon.
        """
        perimeter = 0.0
        for edge in self.edges():
            perimeter += edge.length()

        return perimeter


    def bounding_box(self) -> tuple[Point, Point]:
        """
        Return the minimum bounding rectangle.
        """
        xs = [point.x for point in self._vertices]
        ys = [point.y for point in self._vertices]
        min_point = Point(min(xs), min(ys))
        max_point = Point(max(xs), max(ys))
        return min_point, max_point


    def centroid(self) -> Point:
        return centroid(self._vertices)


    def _signed_area(self) -> float:
        """
        Compute the signed area of the polygon.
        Positive:
            Counter-clockwise vertices
        Negative:
            Clockwise vertices
        """
        area = 0.0
        n = len(self._vertices)

        for i in range(n):
            current = self._vertices[i]
            nxt = self._vertices[(i + 1) % n]
            area += current.x * nxt.y
            area -= nxt.x * current.y

        return area / 2.0


    def transform(self, transformer) -> "Polygon":
        """
        Transform all polygon vertices.
        Parameters
        ----------
        transformer:
            Object with transform_point method.
        """
        transformed_vertices = []

        for point in self._vertices:
            transformed_vertices.append(transformer.transform_point(point))
        return Polygon(transformed_vertices)


    def bounding_box(self) -> BoundingBox:
        """
        Calculate polygon bounding box.
        """
        xs = []
        ys = []
        for point in self._vertices:
            xs.append(point.x)
            ys.append(point.y)

        return BoundingBox(min(xs), min(ys), max(xs), max(ys),)