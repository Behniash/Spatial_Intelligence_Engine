"""
Coordinate transformation utilities.
"""

from __future__ import annotations
from pyproj import Transformer
from src.geometry.point import Point


class UTMTransformer:

    def __init__(self, zone: int):
        """
        Create UTM transformer for a specific zone.

        Parameters
        ----------
        zone : int
            UTM zone number.
        """

        self.zone = zone

        self._transformer = Transformer.from_crs("EPSG:4326", f"EPSG:{32600 + zone}", always_xy=True,)


    @staticmethod
    def calculate_zone(longitude: float) -> int:
        import math
        """
        Calculate UTM zone from longitude.
        """

        return math.floor(longitude // 6) + 31


    @classmethod
    def from_point(cls, point: Point,) -> "UTMTransformer":
        """
        Create transformer automatically from point longitude.
        """
        zone = cls.calculate_zone(point.x)
        return cls(zone)


    def transform_point(self, point: Point,) -> Point:
        """
        Transform geographic point to UTM coordinates.
        """
        x, y = self._transformer.transform(point.x, point.y,)
        return Point(x, y,)