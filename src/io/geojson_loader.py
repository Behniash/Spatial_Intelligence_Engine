"""
geojson_loader.py
Load GeoJSON data into the custom geometry engine.
"""

from __future__ import annotations
from pathlib import Path
import geopandas as gpd
from src.geometry.point import Point
from src.geometry.polygon import Polygon


class GeoJsonLoader:
    """
    Load and manage GeoJSON city boundaries.
    """

    def __init__(self, geojson_path: str | Path,) -> None:

        self._geojson_path = Path(geojson_path)

        if not self._geojson_path.exists():
            raise FileNotFoundError(f"GeoJSON file not found:\n{self._geojson_path}")
        
        self._gdf = gpd.read_file(self._geojson_path)


    def load_city(self, city_name: str, city_column: str = "ADM2_FA",) -> Polygon:
        """
        Load a city as a Polygon.
        """
        city = self._gdf[self._gdf[city_column] == city_name]

        if city.empty:
            raise ValueError(f"City '{city_name}' not found.")

        geometry = city.geometry.iloc[0]

        coords = list(geometry.exterior.coords)

        vertices = [Point(x, y) for x, y in coords]

        return Polygon(vertices)



    def cities(self, city_column: str = "ADM2_FA",) -> list[str]:
        """
        Return all available cities.
        """
        return sorted(self._gdf[city_column].dropna().unique().tolist())


    def search_city(self, text: str, city_column: str = "ADM2_FA",) -> list[str]:
        """
        Search cities by substring.
        """
        cities = self.cities(city_column)
        return [city for city in cities if text in city]