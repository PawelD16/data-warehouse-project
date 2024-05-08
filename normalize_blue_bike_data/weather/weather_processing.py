from typing import Dict, List, Any

import pandas as pd

from utils import column_to_datetime
from weather.weather_condition import WeatherCondition
from weather.weather_dict import WeatherDict


# Dane pogodowe mapowane są na podstawie daty rozpoczęcia przejazdu.
# Powodem jest fakt, że dane o przejazdach taksówką wykonują identyczną operację.
# Przejazdy rowerowe nie trwają długo, więc tym bardziej nie jest to problem.
def process_taxi_ride_csv_file(file_path: str) -> WeatherDict:
    data = pd.read_csv(file_path)

    column_to_datetime(data, "datetime")
    weather_dict = WeatherDict()

    for index, row in data.iterrows():
        weather_dict.add_weather_condition(row["datetime"], WeatherCondition(row))

    return weather_dict


def map_stations_from_bike_csv_files(df: pd.DataFrame, weather_dict: WeatherDict) -> pd.DataFrame:
    data_list: List[Dict[str, Any]] = []

    for index, row in df.iterrows():
        data_list.append(
            weather_dict.get_closest_time_point(row["starttime"])[1].get_dictionary_of()
        )

    dict_df = pd.DataFrame(data_list)

    return pd.concat([df, dict_df], axis=1)


def weather_main(taxi_file_path: str, df: pd.DataFrame) -> pd.DataFrame:
    return map_stations_from_bike_csv_files(
        df,
        process_taxi_ride_csv_file(taxi_file_path)
    )
