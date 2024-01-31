import os
import urllib.request
import zipfile
import pandas as pd
from sqlalchemy.types import Integer, Text, Float

url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
zip_path = "GTFS.zip"
file_path = "GTFS/"
file_name = "stops.txt"
column_picker = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
columns_dType = {"stop_id" : Integer, "stop_name" : Text, "stop_lat" : Float, "stop_lon" : Float, "zone_id" : Integer}


# Data processing
urllib.request.urlretrieve(url, zip_path)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(file_path)

# save to df
stops_file = file_path + file_name
df = pd.read_csv(stops_file, sep=',', decimal='.', index_col=False, usecols=column_picker, encoding='utf-8')

# Only keep stops from zone 2001
df = df[df["zone_id"] == 2001]

# validate data
df = df[(df["stop_lat"] >= -90) & (df["stop_lat"] <= 90) & (df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)]

# Write data into a SQLite database, and set the correct data types
df.to_sql("stops", "sqlite://" + "/gtfs.sqlite", if_exists='replace', dtype=columns_dType, index=False)