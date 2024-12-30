--https://www.hackerrank.com/challenges/weather-observation-station-17/

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
select min(cast(long_w as decimal(10,4))) from station
where lat_n = (select min(lat_n) from station where lat_n> 38.7780);