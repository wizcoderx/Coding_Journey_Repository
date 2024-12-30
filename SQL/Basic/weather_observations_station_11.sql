--https://www.hackerrank.com/challenges/weather-observation-station-11

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

SELECT distinct City FROM STATION WHERE City NOT LIKE '[A,E,I,O,U]%[A,E,I,O,U]'
