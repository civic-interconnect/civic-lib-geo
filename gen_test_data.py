from pathlib import Path

import geopandas as gpd
from shapely.geometry import Polygon

data_dir = Path("tests/data")
data_dir.mkdir(parents=True, exist_ok=True)

# Define a simple polygon and a GeoDataFrame
polygon = Polygon([(-93.0, 45.0), (-93.0, 45.1), (-92.9, 45.1), (-92.9, 45.0), (-93.0, 45.0)])
gdf = gpd.GeoDataFrame([{"name": "Test Area"}], geometry=[polygon], crs="EPSG:4326")

# Save shapefile (writes .shp, .shx, .dbf, etc.)
gdf.to_file(data_dir / "test_shapefile.shp")
print("Shapefile written to tests/data/")
