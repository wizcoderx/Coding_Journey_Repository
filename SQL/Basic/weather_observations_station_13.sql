--https://www.hackerrank.com/challenges/weather-observation-station-13

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select cast(round(sum(lat_n),4) as NUMERIC(12, 4)) from station
where lat_n between 38.7880 and 137.2345;