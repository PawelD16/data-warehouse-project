import math
from typing import Dict, List

from location.location_point import LocationPoint
from utils import distance


class LocationDict:
    def __init__(self):
        self.__locations: Dict[str, List[LocationPoint]] = {}
        self.__locations_pre_mapped: Dict[str, str] = {}

    def add_location_points(self, location_name: str, location_point: LocationPoint) -> None:
        if location_name not in self.__locations:
            self.__locations[location_name] = [location_point]
        else:
            self.__locations[location_name].append(location_point)

    def get_closest_location_name(self, target_point: LocationPoint, target_name: str) -> str:
        if target_name in self.__locations_pre_mapped.keys():
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
                    if dist <= 0:
                        return closest_location

        return closest_location

    def __str__(self) -> str:
        return str(self.__locations)
