--https://www.hackerrank.com/challenges/japan-population

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select sum(population) from city
where countrycode='JPN';