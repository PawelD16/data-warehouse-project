from location_point import LocationPoint


class Ride:
    def __init__(
        self,
        ride_type: str,
        ride_company: str,
        time_of_day: str,
        start: LocationPoint,
        destination: LocationPoint,
    ) -> None:
        self.__ride_type = ride_type
        self.__ride_company = ride_company
        self.__time_of_day = time_of_day
        self.__location_point = start
        self.__destination = destination

    def get_ride_type(self) -> str:
        return self.__ride_type

    def get_ride_company(self) -> str:
        return self.__ride_company

    def get_time_of_day(self) -> str:
        return self.__time_of_day

    def get_start(self) -> LocationPoint:
        return self.__location_point

    def get_destination(self) -> LocationPoint:
        return self.__destination
