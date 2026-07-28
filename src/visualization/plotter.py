"""
Visualization utilities for geometry objects.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from src.geometry.point import Point
from src.geometry.polygon import Polygon


class GeometryPlotter:

    @staticmethod
    def plot_polygon(
        polygon: Polygon,
        show_vertices: bool = False,
        color: str = "steelblue",
        linewidth: float = 2,
        label: str | None = None,
    ) -> None:

        xs = [p.x for p in polygon]
        ys = [p.y for p in polygon]

        plt.plot(
            xs,
            ys,
            color=color,
            linewidth=linewidth,
            label=label,
        )

        if show_vertices:
            plt.scatter(xs, ys, s=15)

    @staticmethod
    def plot_point(point: Point, color: str = "red", size: int = 80, label: str | None = None,) -> None:

        plt.scatter(
            point.x,
            point.y,
            s=size,
            color=color,
            label=label,
        )


    @staticmethod
    def plot_bounding_box(polygon: Polygon, color: str = "green",) -> None:

        min_point, max_point = polygon.bounding_box()

        xs = [
            min_point.x,
            max_point.x,
            max_point.x,
            min_point.x,
            min_point.x,
        ]

        ys = [
            min_point.y,
            min_point.y,
            max_point.y,
            max_point.y,
            min_point.y,
        ]

        plt.plot(
            xs,
            ys,
            linestyle="--",
            color=color,
        )