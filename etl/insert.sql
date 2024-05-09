USE Projekt;

INSERT INTO Months (ID, [MonthName])
VALUES 
(1, 'january'), 
(2, 'february'), 
(3, 'march'),
(4, 'april'), 
(5, 'may'), 
(6, 'june'),
(7, 'july'), 
(8, 'august'), 
(9, 'september'),
(10, 'october'),
(11, 'november'), 
(12, 'december');

INSERT INTO DaysOfWeek (ID, DayOfWeekName)
VALUES 
(1, 'monday'),
(2, 'wednesday'),
(3, 'tuesday'),
(4, 'thursday'),
(5, 'friday'),
(6, 'saturday'),
(7, 'sunday');

-- DIMENSIONS
INSERT INTO DIM_DATE (DateID, [Month], [MonthName], DayOfWeekName, [DayOfMonth])
SELECT DISTINCT
    RideDateTimeToInt / 1000000 AS DateID,
    MONTH(RideDateTime) AS [Month],
    M.[MonthName] AS [MonthName],
    DT.DayOfWeekName AS DayOfWeekName,
    DAY(RideDateTime) AS [DayOfMonth]
FROM BulkCSVImported
LEFT JOIN Months M ON MONTH(RideDateTime) = M.ID
LEFT JOIN DaysOfWeek DT ON DATEPART(WEEKDAY, RideDateTime) = DT.ID
ORDER BY DateID;

INSERT INTO DIM_TIME (TimeID, TimeOfDay, [Hour], [Minute],	[Second])
SELECT DISTINCT
    RideDateTimeToInt % 1000000 AS TimeID,
	CASE 
		WHEN (RideDateTimeToInt / 10000) % 100 >= 4 AND (RideDateTimeToInt / 10000) % 100 < 8 THEN 'morning'
		WHEN (RideDateTimeToInt / 10000) % 100 >= 8 AND (RideDateTimeToInt / 10000) % 100 < 12  THEN 'forenoon'
		WHEN (RideDateTimeToInt / 10000) % 100 >= 12 AND (RideDateTimeToInt / 10000) % 100 < 16 THEN 'noon'
		WHEN (RideDateTimeToInt / 10000) % 100 >= 16 AND (RideDateTimeToInt / 10000) % 100 < 20 THEN 'afternoon'
		WHEN (RideDateTimeToInt / 10000) % 100 >= 20 AND (RideDateTimeToInt / 10000) % 100 < 24  THEN 'evening'
		WHEN (RideDateTimeToInt / 10000) % 100 >= 0 AND (RideDateTimeToInt / 10000) % 100 < 4  THEN 'night'
		ELSE Null
	END AS TimeOfDay,
	(RideDateTimeToInt / 10000) % 100 AS [Hour],
	(RideDateTimeToInt / 100) % 100 AS [Minute],
	RideDateTimeToInt % 100 AS [Second]
FROM BulkCSVImported
ORDER BY TimeID;

INSERT INTO DIM_LOCATION (LocationName)
SELECT DISTINCT
	LocationName
FROM (SELECT Source AS LocationName FROM BulkCSVImported
	UNION ALL
	SELECT Destination AS LocationName FROM BulkCSVImported) AS Locations;

INSERT INTO DIM_WEATHER (TemperatureFahrenheit, ApparentTemperatureFahrenheit,TemperatureCategory, TemperatureCelsius, ApparentTemperatureCelsius,  CloudCover, PrecipProbability, PrecipIntensity, Pressure, MoonPhase, WindSpeed, WindSpeedCategory)
SELECT DISTINCT 
	Temperature as TemperatureFahrenheit,
	ApparentTemperature as ApparentTemperatureFahrenheit,
	CASE
		WHEN ApparentTemperature >= 12  AND ApparentTemperature < 25 THEN 'Very Cold'
		WHEN ApparentTemperature >=25  AND ApparentTemperature < 35 THEN 'Cold'
		WHEN ApparentTemperature >=35  AND ApparentTemperature < 45 THEN 'Chilly'
		WHEN ApparentTemperature >=45  AND ApparentTemperature <= 60 THEN 'Cool'
		ELSE Null
	END AS TemperatureCategory,
	ROUND(((Temperature - 32) * 5.0 / 9.0),2) AS TemperatureCelsius,
	ROUND(((ApparentTemperature - 32) * 5.0 / 9.0),2) AS ApparentTemperatureCelsius,
	CloudCover,
	PrecipProbability,
	PrecipIntensity,
	Pressure,
	MoonPhase, 
	WindSpeed,
	CASE
		WHEN WindSpeed >= 0  AND WindSpeed < 3 THEN 'Very Light Breeze'
		WHEN WindSpeed >= 3  AND WindSpeed < 7 THEN 'Light Breeze'
		WHEN WindSpeed >= 7  AND WindSpeed < 12 THEN 'Gentle Breeze'
		WHEN WindSpeed >= 12  AND WindSpeed <= 15 THEN 'Moderate Breeze'
		ELSE Null
	END AS WindSpeedCategory
FROM BulkCSVImported;

INSERT INTO DIM_CAB (CabCompany, CabProductID, CabProductName)
SELECT DISTINCT 
	CabType AS CabCompany,
	ProductId AS CabProductID,
    ProductName AS CabProductName
FROM BulkCSVImported;

-- FACT
UPDATE BulkCSVImported
SET FK_LocationID_Source = (
    SELECT LocationID
    FROM DIM_LOCATION
    WHERE LocationName = BulkCSVImported.Source
);

UPDATE BulkCSVImported
SET FK_LocationID_Destination = (
    SELECT LocationID
    FROM DIM_LOCATION
    WHERE LocationName = BulkCSVImported.Destination
);

UPDATE BulkCSVImported
SET FK_WeatherID = (
	SELECT WeatherID
	FROM DIM_WEATHER
	WHERE 
		Temperature = BulkCSVImported.Temperature AND
		ApparentTemperature = BulkCSVImported.ApparentTemperature AND
		CloudCover = BulkCSVImported.CloudCover AND
		PrecipProbability = BulkCSVImported.PrecipProbability AND
		Pressure = BulkCSVImported.Pressure AND
		MoonPhase = BulkCSVImported.MoonPhase AND
		WindSpeed = BulkCSVImported.WindSpeed
);

UPDATE BulkCSVImported
SET FK_CabID = (
	SELECT CabID
	FROM DIM_CAB
	WHERE
		CabCompany = BulkCSVImported.CabType AND
		CabProductID = BulkCSVImported.ProductId AND
		CabProductName = BulkCSVImported.ProductName
);

INSERT INTO FACT_RIDE (
	Price, 
	DistanceMiles, 
	SurgeMultiplier,
	FK_DateID, 
	FK_TimeID, 
	FK_LocationID_Source, 
	FK_LocationID_Destination, 
	FK_WeatherID, 
	FK_CabID
)
SELECT 
	Price,
	DistanceMiles,
	SurgeMultiplier,
	RideDateTimeToInt / 1000000 AS FK_DateID,
	RideDateTimeToInt % 1000000 AS FK_TimeID,
	FK_LocationID_Source,
	FK_LocationID_Destination,
	FK_WeatherID, 
	FK_CabID
FROM BulkCSVImported;