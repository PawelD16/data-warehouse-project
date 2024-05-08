import math
from datetime import datetime, timedelta
from typing import List, TypeVar, Dict

import pandas as pd
import csv

from location.location_point import LocationPoint

K = TypeVar('K')
V = TypeVar('V')


def filter_files_by_date(
        file_paths: List[str], date_column_name: str, start_date: datetime, end_date: datetime
) -> pd.DataFrame:
    combined_data = pd.DataFrame()

    for file_path in file_paths:
        data = pd.read_csv(file_path)

        data[date_column_name] = pd.to_datetime(data[date_column_name])
        filtered_data = data[(data[date_column_name] >= start_date) & (data[date_column_name] <= end_date)]

        combined_data = pd.concat([combined_data, filtered_data], ignore_index=True)

    return combined_data


def add_to_dict_if_not_exists(dictionary: Dict[K, V], key: K, value: V) -> Dict[K, V]:
    if key not in dictionary.keys():
        dictionary[key] = value

    return dictionary


def distance(point1: LocationPoint, point2: LocationPoint):
    return math.sqrt(
        (point1.get_latitude() - point2.get_latitude()) ** 2 + (point1.get_longitude() - point2.get_longitude()) ** 2
    )


def remove_commas_inside_quotes(input_csv_path: str, output_csv_path: str) -> None:
    with open(input_csv_path, 'r', newline='') as infile, open(output_csv_path, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            new_row = []
            for field in row:
                field = field.replace(',', '')
                new_row.append(field)
            writer.writerow(new_row)


def remove_commas(df: pd.DataFrame) -> pd.DataFrame:
    return df.replace(',', '', regex=True)


def column_to_datetime(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    df[column_name] = pd.to_datetime(df[column_name])
    return df


def round_to_nearest_quarter(dt: datetime) -> datetime:
    return datetime(dt.year, dt.month, dt.day, dt.hour, 15 * (dt.minute // 15))


def round_to_nearest_minute(date_time: datetime) -> datetime:
    return (date_time + timedelta(seconds=30)).replace(second=0, microsecond=0)
