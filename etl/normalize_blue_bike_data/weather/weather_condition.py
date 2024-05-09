from typing import Any, Dict

import pandas as pd


class WeatherCondition:
    def __init__(self, row: pd.Series) -> None:
        if row is None:
            raise ValueError("row cannot be None")

        temp_row = self.__create_row_dict(row)
        if None in temp_row.values():
            raise ValueError("weather conditions cannot be None")

        self.__row: Dict[str, Any] = temp_row

    def get_value(self, key: str) -> Any:
        return self.__row[key]

    def get_dictionary_of(self) -> Dict[str, Any]:
        return self.__row

    @staticmethod
    def __create_row_dict(row: pd.Series) -> Dict[str, Any]:
        return {
            "temperature": row["temperature"],
            "apparentTemperature": row["apparentTemperature"],
            "short_summary": row["short_summary"],
            "long_summary": row["long_summary"],
            "precipIntensity": row["precipIntensity"],
            "precipProbability": row["precipProbability"],
            "humidity": row["humidity"],
            "windSpeed": row["windSpeed"],
            "windGust": row["windGust"],
            "windGustTime": row["windGustTime"],
            "visibility": row["visibility"],
            "temperatureHigh": row["temperatureHigh"],
            "temperatureHighTime": row["temperatureHighTime"],
            "temperatureLow": row["temperatureLow"],
            "temperatureLowTime": row["temperatureLowTime"],
            "apparentTemperatureHigh": row["apparentTemperatureHigh"],
            "apparentTemperatureHighTime": row["apparentTemperatureHighTime"],
            "apparentTemperatureLow": row["apparentTemperatureLow"],
            "apparentTemperatureLowTime": row["apparentTemperatureLowTime"],
            "icon": row["icon"],
            "dewPoint": row["dewPoint"],
            "pressure": row["pressure"],
            "windBearing": row["windBearing"],
            "cloudCover": row["cloudCover"],
            "uvIndex": row["uvIndex"],
            "visibility.1": row["visibility.1"],
            "ozone": row["ozone"],
            "sunriseTime": row["sunriseTime"],
            "sunsetTime": row["sunsetTime"],
            "moonPhase": row["moonPhase"],
            "precipIntensityMax": row["precipIntensityMax"],
            "uvIndexTime": row["uvIndexTime"],
            "temperatureMin": row["temperatureMin"],
            "temperatureMinTime": row["temperatureMinTime"],
            "temperatureMax": row["temperatureMax"],
            "temperatureMaxTime": row["temperatureMaxTime"],
            "apparentTemperatureMin": row["apparentTemperatureMin"],
            "apparentTemperatureMinTime": row["apparentTemperatureMinTime"],
            "apparentTemperatureMax": row["apparentTemperatureMax"],
            "apparentTemperatureMaxTime": row["apparentTemperatureMaxTime"]
        }

    def __str__(self) -> str:
        return str(self.__row)
