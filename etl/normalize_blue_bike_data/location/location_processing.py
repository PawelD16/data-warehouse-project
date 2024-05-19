from datetime import datetime, time
from typing import List, Dict

import pandas as pd

from location.location_dict import LocationDict
from location.location_point import LocationPoint
from utils import filter_files_by_date, column_to_datetime


def process_taxi_ride_csv_file(file_path: str) -> (LocationDict, datetime, datetime):
    data = pd.read_csv(file_path)

    column_to_datetime(data, "datetime")
    location_dict = LocationDict()

    min_date = data["datetime"].min()
    max_date = data["datetime"].max()

    center_point_location = {
        "Haymarket Square": LocationPoint(42.361583, -71.056083),
        "Boston University": LocationPoint(42.3505, -71.1054),
        "Theatre District": LocationPoint(42.3503, -71.0627),
        "Back Bay": LocationPoint(42.3503, -71.0809),
        "Financial District": LocationPoint(42.3557, -71.0551),
        "Beacon Hill": LocationPoint(42.3588, -71.0707),
        "Northeastern University": LocationPoint(42.3398, -71.0892),
        "West End": LocationPoint(42.3644, -71.0639),
        "South Station": LocationPoint(42.3523, -71.0552),
        "North Station": LocationPoint(42.3656, -71.0616),
        "North End": LocationPoint(42.3647, -71.0542),
        "Fenway": LocationPoint(42.3467, -71.0972)
    }

    for name, location_point in center_point_location.items():
        location_dict.add_location_points(name, location_point)
    """
    Latitude and longitude aren't good to map with because they do not correspond to pick up locations.
    Same point is mapped to different locations. So we map to the center point.
         
    for index, row in data.iterrows():
        # Podawana wysokość i szerokość geograficzna dotyczą 'source'.
        # Zawiera wszystkie lokalizacje, więc nie mamy problemu, że nie używane jest destination
        location_dict.add_location_points(
            row["source"],
            LocationPoint(row["latitude"], row["longitude"])
        )
    """

    return location_dict, min_date, max_date


def map_stations_from_bike_csv_files(data: pd.DataFrame, location_dict: LocationDict) -> Dict[str, str]:
    station_to_district: Dict[str, str] = {}

    for index, row in data.iterrows():
        start_station_point = LocationPoint(
            row["start station latitude"],
            row["start station longitude"]
        )

        end_station_point = LocationPoint(
            row["end station latitude"],
            row["end station longitude"]
        )

        start_station = row["start station name"]
        end_station = row["end station name"]

        if start_station not in station_to_district.values():
            station_to_district[start_station] = location_dict.get_closest_location_name(
                start_station_point,
                start_station
            )

        if end_station not in station_to_district.values():
            station_to_district[end_station] = location_dict.get_closest_location_name(
                end_station_point,
                end_station
            )

    return station_to_district


def location_main(taxi_csv_path: str, bike_csv_paths: List[str]) -> pd.DataFrame:
    (location_dict, min_date, max_date) = process_taxi_ride_csv_file(taxi_csv_path)

    bike_df = filter_files_by_date(
        bike_csv_paths,
        "starttime",
        datetime.combine(min_date, time.min),
        datetime.combine(max_date, time.max)
    )

    stations_to_districts = map_stations_from_bike_csv_files(bike_df, location_dict)

    bike_df["source"] = bike_df["start station name"].map(stations_to_districts)
    bike_df["destination"] = bike_df["end station name"].map(stations_to_districts)

    return bike_df
