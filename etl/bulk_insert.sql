USE Projekt;

BULK 
INSERT BulkCSVTaxiImported
FROM 'C:\Users\stud\Desktop\projekt\data\rideshare_kaggle_cleaned.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2
);

BULK
INSERT BulkCSVBikeImported
FROM 'C:\Users\stud\Desktop\projekt\data\bluebike-normalized_cleaned.csv'
WITH
(
    FORMAT = 'CSV',
    FIRSTROW = 2
);

INSERT INTO BulkCSVImported (
	RideDateTime,
    Source,
    Destination,
    CabType,
    ProductId,
    ProductName,
    PriceNVarChar,
    DistanceMiles,
    SurgeMultiplier,
    Latitude,
    Longitude,
    Temperature,
    ApparentTemperature,
    ShortSummary,
    PrecipIntensity,
    PrecipProbability,
    Humidity,
    WindSpeed,
    WindGust,
    Visibility,
    TemperatureHigh,
    TemperatureLow,
    ApparentTemperatureHigh,
    ApparentTemperatureLow,
    Icon,
    DewPoint,
    Pressure,
    WindBearing,
    CloudCover,
    UvIndex,
    Ozone,
    SunriseTime,
    SunsetTime,
    MoonPhase,
    PrecipIntensityMax,
    TemperatureMin,
    TemperatureMax,
    ApparentTemperatureMin,
    ApparentTemperatureMax
)
SELECT
    RideDateTime,
    Source,
    Destination,
    CabType,
    ProductId,
    ProductName,
    PriceNVarChar,
    DistanceMiles,
    SurgeMultiplier,
    Latitude,
    Longitude,
    Temperature,
    ApparentTemperature,
    ShortSummary,
    PrecipIntensity,
    PrecipProbability,
    Humidity,
    WindSpeed,
    WindGust,
    Visibility,
    TemperatureHigh,
    TemperatureLow,
    ApparentTemperatureHigh,
    ApparentTemperatureLow,
    Icon,
    DewPoint,
    Pressure,
    WindBearing,
    CloudCover,
    UvIndex,
    Ozone,
    SunriseTime,
    SunsetTime,
    MoonPhase,
    PrecipIntensityMax,
    TemperatureMin,
    TemperatureMax,
    ApparentTemperatureMin,
    ApparentTemperatureMax
FROM BulkCSVTaxiImported;

INSERT INTO BulkCSVImported (
	RideDateTime,
    Source,
    Destination,
    CabType,
    ProductId,
    ProductName,
    PriceNVarChar,
    DistanceMiles,
    SurgeMultiplier,
    Latitude,
    Longitude,
    Temperature,
    ApparentTemperature,
    ShortSummary,
    PrecipIntensity,
    PrecipProbability,
    Humidity,
    WindSpeed,
    WindGust,
    Visibility,
    TemperatureHigh,
    TemperatureLow,
    ApparentTemperatureHigh,
    ApparentTemperatureLow,
    Icon,
    DewPoint,
    Pressure,
    WindBearing,
    CloudCover,
    UvIndex,
    Ozone,
    SunriseTime,
    SunsetTime,
    MoonPhase,
    PrecipIntensityMax,
    TemperatureMin,
    TemperatureMax,
    ApparentTemperatureMin,
    ApparentTemperatureMax
) 
SELECT
	Starttime AS RideDateTime,
	Source,
    Destination,
	'Bike' AS CabType,
	UserType AS ProductId,
	UserType AS ProductName,
	'NA' AS PriceNVarChar,
	NULL AS DistanceMiles,
    NULL AS SurgeMultiplier,
	StartStationLatitude AS Latitude,
	StartStationLongitude AS Longitude,   
    Temperature,
    ApparentTemperature,
    ShortSummary,
    PrecipIntensity,
    PrecipProbability,
    Humidity,
    WindSpeed,
    WindGust,
    Visibility,
    TemperatureHigh,
    TemperatureLow,
    ApparentTemperatureHigh,
    ApparentTemperatureLow,
    Icon,
    DewPoint,
    Pressure,
    WindBearing,
    CloudCover,
    UvIndex,
    Ozone,
    SunriseTime,
    SunsetTime,
    MoonPhase,
    PrecipIntensityMax,
    TemperatureMin,
    TemperatureMax,
    ApparentTemperatureMin,
    ApparentTemperatureMax
FROM BulkCSVBikeImported;

ALTER TABLE BulkCSVImported
ADD RideDateTimeToInt AS CONVERT(BIGINT, FORMAT(RideDateTime, 'yyyyMMddHHmmss'));

ALTER TABLE BulkCSVImported
ADD Price AS 
    CASE 
        WHEN PriceNVarChar = 'NA' THEN NULL
        ELSE CONVERT(FLOAT, PriceNVarChar)
    END;

ALTER TABLE BulkCSVImported
ADD FK_LocationID_Source TINYINT,
FK_LocationID_Destination TINYINT,
FK_WeatherID SMALLINT,
FK_CabID TINYINT;