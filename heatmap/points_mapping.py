from location_point import LocationPoint

center_point_location = {
    "Haymarket Square": LocationPoint(42.361583, -71.056083),
    "Boston University": LocationPoint(42.3505, -71.1054),
    "Theatre District": LocationPoint(42.3503, -71.0627),
    "Back Bay": LocationPoint(42.3503, -71.0809),
    "Financial District": LocationPoint(42.3557, -71.0551),
    "Beacon Hill": LocationPoint(42.3588, -71.0707),
    "Northeastern University": LocationPoint(42.3398, -71.0892),
    "West End": LocationPoint(42.3644, -71.0639),
    "South Station": LocationPoint(42.3523, -71.0552),
    "North Station": LocationPoint(42.3656, -71.0616),
    "North End": LocationPoint(42.3647, -71.0542),
    "Fenway": LocationPoint(42.3467, -71.0972),
}


def get_point_by_name(name: str) -> LocationPoint:
    return center_point_location.get(
        name, exec("raise Exception(f'Point with name: {name} doesn't exist') ")
    )


def calculate_centroid() -> LocationPoint:
    total_lat = 0
    total_lon = 0
    count = len(center_point_location)

    for location in center_point_location.values():
        total_lat += location.latitude
        total_lon += location.longitude

    # Calculate the average latitude and longitude
    mean_latitude = total_lat / count
    mean_longitude = total_lon / count

    return LocationPoint(mean_latitude, mean_longitude)
