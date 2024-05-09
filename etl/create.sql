USE Projekt;

-- DIRTY
CREATE TABLE BulkCSVTaxiImported (
	ID NVARCHAR(50),
    RideTimestamp FLOAT,
    RideHour TINYINT,
    RideDay TINYINT,
    RideMonth TINYINT,
    RideDateTime DATETIME2,
    Timezone NVARCHAR(50),
    Source NVARCHAR(50),
    Destination NVARCHAR(50),
    CabType NVARCHAR(50),
    ProductId NVARCHAR(50),
    ProductName NVARCHAR(50),
    PriceNVarChar NVARCHAR(50), -- nie float ponieważ mamy czasem brak ceny. Zmienione zostanie na float z nullami w tabeli faktów
    DistanceMiles FLOAT,
    SurgeMultiplier FLOAT,
    Latitude FLOAT,
    Longitude FLOAT,
    Temperature FLOAT,
    ApparentTemperature FLOAT,
    ShortSummary NVARCHAR(50),
    LongSummary NVARCHAR(100),
    PrecipIntensity FLOAT,
    PrecipProbability FLOAT,
    Humidity FLOAT,
    WindSpeed FLOAT,
    WindGust FLOAT,
    WindGustTime INT,
    Visibility FLOAT,
    TemperatureHigh FLOAT,
    TemperatureHighTime INT,
    TemperatureLow FLOAT,
    TemperatureLowTime INT,
    ApparentTemperatureHigh FLOAT,
    ApparentTemperatureHighTime FLOAT,
    ApparentTemperatureLow FLOAT,
    ApparentTemperatureLowTime INT,
    Icon NVARCHAR(50),
    DewPoint FLOAT,
    Pressure FLOAT,
    WindBearing SMALLINT,
    CloudCover FLOAT,
    UvIndex TINYINT,
    Visibility_1_to_10 FLOAT,
    Ozone FLOAT,
    SunriseTime INT,
    SunsetTime INT,
    MoonPhase FLOAT,
    PrecipIntensityMax FLOAT,
    UvIndexTime INT,
    TemperatureMin FLOAT,
    TemperatureMinTime INT,
    TemperatureMax FLOAT,
    TemperatureMaxTime INT,
    ApparentTemperatureMin FLOAT,
    ApparentTemperatureMinTime INT,
    ApparentTemperatureMax FLOAT,
    ApparentTemperatureMaxTime INT,
);

CREATE TABLE BulkCSVBikeImported (
	Tripduration INT,
	Starttime DATETIME2,
	Stoptime DATETIME2,
	StartStationId INT,
	StartStationName NVARCHAR(100),
	StartStationLatitude FLOAT,
	StartStationLongitude FLOAT,
	EndStationId INT,
	EndStationName NVARCHAR(100),
	EndStationLatitude FLOAT,
	EndStationLongitude FLOAT,
	BikeId INT,
	UserType NVARCHAR(20),
	BirthYear FLOAT, -- czasem to float (???)
	gender TINYINT,
    Source NVARCHAR(50),
    Destination NVARCHAR(50),
    Temperature FLOAT,
    ApparentTemperature FLOAT,
    ShortSummary NVARCHAR(50),
    LongSummary NVARCHAR(100),
    PrecipIntensity FLOAT,
    PrecipProbability FLOAT,
    Humidity FLOAT,
    WindSpeed FLOAT,
    WindGust FLOAT,
    WindGustTime INT,
    Visibility FLOAT,
    TemperatureHigh FLOAT,
    TemperatureHighTime INT,
    TemperatureLow FLOAT,
    TemperatureLowTime INT,
    ApparentTemperatureHigh FLOAT,
    ApparentTemperatureHighTime FLOAT,
    ApparentTemperatureLow FLOAT,
    ApparentTemperatureLowTime INT,
    Icon NVARCHAR(50),
    DewPoint FLOAT,
    Pressure FLOAT,
    WindBearing SMALLINT,
    CloudCover FLOAT,
    UvIndex TINYINT,
    Visibility_1_to_10 FLOAT,
    Ozone FLOAT,
    SunriseTime INT,
    SunsetTime INT,
    MoonPhase FLOAT,
    PrecipIntensityMax FLOAT,
    UvIndexTime INT,
    TemperatureMin FLOAT,
    TemperatureMinTime INT,
    TemperatureMax FLOAT,
    TemperatureMaxTime INT,
    ApparentTemperatureMin FLOAT,
    ApparentTemperatureMinTime INT,
    ApparentTemperatureMax FLOAT,
    ApparentTemperatureMaxTime INT,
);

CREATE TABLE BulkCSVImported (
    RideDateTime DATETIME2,
    Source NVARCHAR(50),
    Destination NVARCHAR(50),
    CabType NVARCHAR(20),
    ProductId NVARCHAR(50),
    ProductName NVARCHAR(50),
    PriceNVarChar NVARCHAR(50), -- nie float ponieważ mamy czasem brak ceny. Zmienione zostanie na float z nullami w tabeli faktów
    DistanceMiles FLOAT,
    SurgeMultiplier FLOAT,
    Latitude FLOAT,
    Longitude FLOAT,
    Temperature FLOAT,
    ApparentTemperature FLOAT,
    ShortSummary NVARCHAR(50),
    PrecipIntensity FLOAT,
    PrecipProbability FLOAT,
    Humidity FLOAT,
    WindSpeed FLOAT,
    WindGust FLOAT,
    Visibility FLOAT,
    TemperatureHigh FLOAT,
    TemperatureLow FLOAT,
    ApparentTemperatureHigh FLOAT,
    ApparentTemperatureLow FLOAT,
    Icon NVARCHAR(50),
    DewPoint FLOAT,
    Pressure FLOAT,
    WindBearing SMALLINT,
    CloudCover FLOAT,
    UvIndex TINYINT,
    Ozone FLOAT,
    SunriseTime INT,
    SunsetTime INT,
    MoonPhase FLOAT,
    PrecipIntensityMax FLOAT,
    TemperatureMin FLOAT,
    TemperatureMax FLOAT,
    ApparentTemperatureMin FLOAT,
    ApparentTemperatureMax FLOAT
);

-- HELPERS
CREATE TABLE Months (
    ID INT PRIMARY KEY,
    [MonthName] VARCHAR(20)
);

CREATE TABLE DaysOfWeek (
    ID INT PRIMARY KEY,
    DayOfWeekName VARCHAR(20)
);

-- DIMENSIONS
CREATE TABLE DIM_DATE (
    DateID INT PRIMARY KEY,
    [Month] INT,
    [MonthName] VARCHAR(20),
    DayOfWeekName VARCHAR(20),
    [DayOfMonth] TINYINT,
);

CREATE TABLE DIM_TIME (
	TimeID INT PRIMARY KEY,
	TimeOfDay VARCHAR(20),
	[Hour] TINYINT,
	[Minute] TINYINT,
	[Second] TINYINT,
);

CREATE TABLE DIM_LOCATION (
	LocationID TINYINT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	LocationName NVARCHAR(50)
);

CREATE TABLE DIM_WEATHER (
	WeatherID SMALLINT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	TemperatureFahrenheit FLOAT,
	ApparentTemperatureFahrenheit FLOAT,
	TemperatureCategory VARCHAR(25),
	TemperatureCelsius FLOAT,
	ApparentTemperatureCelsius FLOAT,
	CloudCover FLOAT,
	PrecipProbability FLOAT,
	PrecipIntensity FLOAT,
	Pressure FLOAT,
	MoonPhase FLOAT,
	WindSpeed FLOAT,
	WindSpeedCategory VARCHAR(25)
);

CREATE TABLE DIM_CAB (
	CabID TINYINT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	CabCompany NVARCHAR(50),
	CabProductID NVARCHAR(50),
	CabProductName NVARCHAR(50)
);

-- FACTS
CREATE TABLE FACT_RIDE (
	RideID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	Price FLOAT,
	DistanceMiles FLOAT,
	SurgeMultiplier FLOAT,
	FK_DateID INT,
	FK_TimeID INT,
	FK_LocationID_Source TINYINT,
	FK_LocationID_Destination TINYINT,
	FK_WeatherID SMALLINT,
	FK_CabID TINYINT
);