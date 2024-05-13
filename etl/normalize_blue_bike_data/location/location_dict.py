import math
from collections import defaultdict
from typing import Dict, List

from location.location_point import LocationPoint
from utils import distance


class LocationDict:
    def __init__(self) -> None:
        self.__locations: Dict[str, List[LocationPoint]] = defaultdict(list)
        self.__locations_pre_mapped: Dict[str, str] = {}

    def add_location_points(self, location_name: str, location_point: LocationPoint) -> None:
        self.__locations[location_name].append(location_point)

    def get_closest_location_name(self, target_point: LocationPoint, target_name: str) -> str:
        if target_name in self.__locations_pre_mapped:
            return self.__locations_pre_mapped[target_name]

        closest_location = None
        min_distance = math.inf

        for name, points in self.__locations.items():
            for point in points:
                dist = distance(point, target_point)
                if dist < min_distance:
                    min_distance = dist
                    closest_location = name

        self.__locations_pre_mapped[target_name] = closest_location
        return closest_location

    def __str__(self) -> str:
        return (f"Locations: {', '.join(f"{key}: {len(value)}" for key, value in self.__locations.items())} \n"
                f" Locations pre-mapped {self.__locations_pre_mapped}")
