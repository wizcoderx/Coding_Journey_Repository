--https://www.hackerrank.com/challenges/weather-observation-station-7

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select distinct city from station
where (city like "%A" or  city like "%E" or city like "%I" or city like "%O" or city like "%U");