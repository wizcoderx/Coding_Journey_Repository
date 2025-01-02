--https://www.hackerrank.com/challenges/african-cities

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select city.name from city
inner join country on city.countrycode = country.code where country.continent = 'Africa';