class LocationPoint:
    def __init__(self, latitude: float, longitude: float):
        if latitude is None or longitude is None:
            raise ValueError("latitude and longitude cannot ne None")

        self.__latitude: float = latitude
        self.__longitude: float = longitude

    def get_latitude(self) -> float:
        return self.__latitude

    def get_longitude(self) -> float:
        return self.__longitude

    def __str__(self) -> str:
        return f"Latitude: {self.__latitude}, Longitude: {self.__longitude}"
