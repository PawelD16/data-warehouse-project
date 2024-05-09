﻿USE Projekt;

ALTER TABLE FACT_RIDE
ADD
CONSTRAINT FK_FACT_RIDE_DIM_DATE FOREIGN KEY(FK_DateID) REFERENCES DIM_DATE(DateID) ON DELETE NO ACTION,
CONSTRAINT FK_FACT_RIDE_DIM_TIME FOREIGN KEY(FK_TimeID) REFERENCES DIM_TIME(TimeID) ON DELETE NO ACTION,
CONSTRAINT FK_FACT_RIDE_DIM_LOCATION_SOURCE FOREIGN KEY(FK_LocationID_Source) REFERENCES DIM_LOCATION(LocationID) ON DELETE NO ACTION,
CONSTRAINT FK_FACT_RIDE_DIM_LOCATION_DESTINATION FOREIGN KEY(FK_LocationID_Destination) REFERENCES DIM_LOCATION(LocationID) ON DELETE NO ACTION,
CONSTRAINT FK_FACT_RIDE_DIM_WEATHER FOREIGN KEY(FK_WeatherID) REFERENCES DIM_WEATHER(WeatherID) ON DELETE NO ACTION,
CONSTRAINT FK_FACT_RIDE_DIM_CAB FOREIGN KEY(FK_CabID) REFERENCES DIM_CAB(CabID) ON DELETE NO ACTION;