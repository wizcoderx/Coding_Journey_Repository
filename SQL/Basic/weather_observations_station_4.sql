--https://www.hackerrank.com/challenges/weather-observation-station-4

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select ((select count(city) from station)- (select count(distinct city) from station)) as ans;