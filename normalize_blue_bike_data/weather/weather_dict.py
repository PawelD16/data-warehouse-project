from datetime import datetime, timedelta
from typing import Dict, Tuple, Callable

from utils import add_to_dict_if_not_exists, round_to_nearest_quarter
from weather.weather_condition import WeatherCondition


# Zaokrąglanie czasu (__time_rounding).
# Znacząco przyspiesza działanie.
# Pogoda nie jest aż tak zmienna.

class WeatherDict:
    def __init__(self) -> None:
        self.__weather_dict: Dict[datetime, WeatherCondition] = {}
        self.__time_rounding: Callable[[datetime], datetime] = round_to_nearest_quarter

    def add_weather_condition(self, weather_date: datetime, row: WeatherCondition) -> None:
        add_to_dict_if_not_exists(
            self.__weather_dict,
            self.__time_rounding(weather_date),
            row
        )

    def get_closest_time_point(self, target: datetime) -> Tuple[datetime, WeatherCondition]:
        target_normalized = self.__time_rounding(target)

        if target_normalized in self.__weather_dict.keys():
            return target, self.__weather_dict[target_normalized]

        closest_time = None
        closest_condition = None
        min_time_difference = timedelta.max

        for datetime_point, condition in self.__weather_dict.items():
            time_difference = abs(datetime_point - target_normalized)
            if time_difference < min_time_difference:
                min_time_difference = time_difference
                closest_time = datetime_point
                closest_condition = condition
                if time_difference == 0:
                    return closest_time, closest_condition

        return closest_time, closest_condition

    def __str__(self) -> str:
        return str(self.__weather_dict)
