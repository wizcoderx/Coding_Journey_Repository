--https://www.hackerrank.com/challenges/weather-observation-station-2

SELECT
    CAST(ROUND(SUM(LAT_N), 2) AS NUMERIC(12, 2)) AS lat,
    CAST(ROUND(SUM(LONG_W), 2) AS NUMERIC(12, 2)) AS lon
FROM STATION;
