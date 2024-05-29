import os
from typing import Callable

import pyodbc
import folium
from folium.plugins import HeatMap
from dotenv import load_dotenv

from location_point import LocationPoint
from ride_data import Ride
from points_mapping import get_point_by_name, calculate_centroid

load_dotenv()

db_driver = os.getenv("DB_DRIVER")
db_server = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")

conn_str = f"DRIVER={db_driver};SERVER={db_server};DATABASE={db_name};Trusted_Connection=yes"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

query = """
        SELECT 
            DIM_TRANSPORT.TransportType     AS RideType,
            DIM_TRANSPORT.TransportCompany  AS RideCompany,
            DIM_TIME.TimeOfDay              AS TimeOfDay,
            L1.LocationName                 AS Destination,
            L2.LocationName                 AS Source
        FROM FACT_RIDE 
        JOIN DIM_LOCATION L1    ON FK_LocationID_Destination    = L1.LocationID
        JOIN DIM_LOCATION L2    ON FK_LocationID_Source         = L2.LocationID
        JOIN DIM_TIME           ON FK_TimeID                    = DIM_TIME.TimeID
        JOIN DIM_TRANSPORT      ON FK_TransportID               = DIM_TRANSPORT.TransportID;
        """

cursor.execute(query)

data = cursor.fetchall()


def get_fact_ride_data(
    file_name: str,
    get_location: Callable[[Ride], LocationPoint],
    filter_fn: Callable[[Ride], bool],
) -> None:

    locations = [
        Ride(
            ride_type=row[0],
            ride_company=row[1],
            time_of_day=row[2],
            start=get_point_by_name(row[3]),
            destination=get_point_by_name(row[4]),
        )
        for row in data
    ]

    locations = filter(filter_fn, locations)

    centroid = calculate_centroid()

    map_of_boston = folium.Map(
        location=[centroid.get_latitude(), centroid.get_longitude()], zoom_start=15
    )

    HeatMap(
        [
            (get_location(loc).get_latitude(), get_location(loc).get_longitude())
            for loc in locations
        ]
    ).add_to(map_of_boston)

    map_of_boston.save(file_name + ".html")
