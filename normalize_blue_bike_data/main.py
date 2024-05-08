import sys
from typing import List

from location.location_processing import location_main
from utils import remove_commas
from weather.weather_processing import weather_main

DEFAULT_TAXI_CSV_PATH = "../data/rideshare_kaggle.csv"
DEFAULT_CSV_OUTPUT = "../data/bluebike-normalized.csv"
DEFAULT_BIKE_CSV_PATHS = [
    "../data/201811-bluebikes-tripdata.csv",
    "../data/201812-bluebikes-tripdata.csv"
]


def main(
        taxi_csv_path: str, bike_csv_paths: List[str]
) -> None:
    bike_df, taxi_df = weather_main(
        taxi_csv_path,
        location_main(taxi_csv_path, bike_csv_paths)
    )

    remove_commas(bike_df).to_csv("cleaned_" + DEFAULT_CSV_OUTPUT, index=False)
    remove_commas(taxi_df).to_csv("cleaned_" + taxi_csv_path, index=False)


def read_argv_with_defaults(argv: List[str]) -> (str, List[str]):
    if len(argv) < 3:
        return DEFAULT_TAXI_CSV_PATH, DEFAULT_BIKE_CSV_PATHS

    return argv[1], argv[2:]


if __name__ == "__main__":
    main(*read_argv_with_defaults(sys.argv))
