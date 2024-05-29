from fact_ride import get_fact_ride_data
from location_point import LocationPoint
from ride_data import Ride

times_of_day = ["morning", "forenoon", "noon", "afternoon", "evening", "night"]
ride_companies = ["Uber", "Lyft", "BlueBike"]
ride_types = ["Taxi", "Bike"]


def get_start(ride: Ride) -> LocationPoint:
    return ride.get_start()


def get_destination(ride: Ride) -> LocationPoint:
    return ride.get_destination()


def get_ride_types(ride: Ride, ride_type: str, time_of_day: str) -> bool:
    return (
        ride.get_ride_type().upper() == ride_type.upper()
        and ride.get_time_of_day().upper() == time_of_day.upper()
    )


def get_company(ride: Ride, name: str, time_of_day: str) -> bool:
    return (
        ride.get_ride_company().upper() == name.upper()
        and ride.get_time_of_day().upper() == time_of_day.upper()
    )


def get_all() -> None:
    for time_of_day in times_of_day:
        for ride_type in ride_types:
            get_fact_ride_data(
                f"{ride_type.lower()}_start_{time_of_day.lower()}",
                get_start,
                lambda ride: get_ride_types(ride, ride_type, time_of_day),
            )

            get_fact_ride_data(
                f"{ride_type.lower()}_destination_{time_of_day.lower()}",
                get_destination,
                lambda ride: get_ride_types(ride, ride_type, time_of_day),
            )

        for ride_company in ride_companies:
            get_fact_ride_data(
                f"{ride_company.lower()}_start_{time_of_day.lower()}",
                get_start,
                lambda ride: get_company(ride, ride_company, time_of_day),
            )

            get_fact_ride_data(
                f"{ride_company.lower()}_destination_{time_of_day.lower()}",
                get_destination,
                lambda ride: get_ride_types(ride, ride_company, time_of_day),
            )


if __name__ == "__main__":
    get_all()
