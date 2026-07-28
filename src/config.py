"""
Project-wide path configuration.
"""

from pathlib import Path

# Spatial_Intelligence_Engine/
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# data/
DATA_DIR = PROJECT_ROOT / "data"

# data/raw/
RAW_DATA_DIR = DATA_DIR / "raw"

# data/processed/
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# notebooks/
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# tests/
TESTS_DIR = PROJECT_ROOT / "tests"