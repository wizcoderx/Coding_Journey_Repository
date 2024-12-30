--https://www.hackerrank.com/challenges/weather-observation-station-16/

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT MIN(CAST(LAT_N AS DECIMAL(10, 4)))
FROM STATION
WHERE LAT_N > 38.7780;

