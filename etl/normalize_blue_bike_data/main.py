import os
import sys
from typing import List

from location.location_processing import location_main
from utils import remove_commas, add_suffix_to_filename
from weather.weather_processing import weather_main

DEFAULT_TAXI_CSV_PATH = "../../data/rideshare_kaggle.csv"
DEFAULT_CSV_OUTPUT = "../../data/bluebike-normalized.csv"
DEFAULT_BIKE_CSV_PATHS = [
    "../../data/201811-bluebikes-tripdata.csv",
    "../../data/201812-bluebikes-tripdata.csv"
]

DEFAULT_CLEANED_SUFFIX = "_cleaned"


def main(
        taxi_csv_path: str, bike_csv_paths: List[str]
) -> None:
    if all([os.path.isfile(add_suffix_to_filename(file, DEFAULT_CLEANED_SUFFIX))
            for file in [DEFAULT_CSV_OUTPUT, DEFAULT_CSV_OUTPUT]]):
        return

    bike_df, taxi_df = weather_main(
        taxi_csv_path,
        location_main(taxi_csv_path, bike_csv_paths)
    )

    remove_commas(bike_df).to_csv(
        add_suffix_to_filename(DEFAULT_CSV_OUTPUT, DEFAULT_CLEANED_SUFFIX), index=False
    )
    remove_commas(taxi_df).to_csv(
        add_suffix_to_filename(taxi_csv_path, DEFAULT_CLEANED_SUFFIX), index=False
    )


def read_argv_with_defaults(argv: List[str]) -> (str, List[str]):
    if len(argv) < 3:
        return DEFAULT_TAXI_CSV_PATH, DEFAULT_BIKE_CSV_PATHS

    return argv[1], argv[2:]


if __name__ == "__main__":
    main(*read_argv_with_defaults(sys.argv))
    sys.exit(0)
