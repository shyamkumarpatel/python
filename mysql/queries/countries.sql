/* ***********
Query:
1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)
************** */
Select
	cts.name, l.language, l.percentage
From countries cts
left join languages l on cts.code = l.country_code
Where l.language = 'Slovene'
ORDER BY l.Percentage DESC;

/* ***********
Query:
2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)
************** */
Select
	cts.name AS country, COUNT(*) AS "total number of cities"
From countries cts
INNER join cities cs on cts.code = cs.country_code
GROUP BY cts.name
ORDER BY count(*) DESC;

/* ***********
Query:
3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)
************** */
Select
	cts.name, cts.population, cts.country_id
From cities cts
WHERE cts.population > 500000 and cts.country_id = (select id from world.countries where name = 'Mexico')
ORDER BY cts.population DESC;

/* ***********
Query:
4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
************** */
select
	cts.name, l.language, l.percentage
from languages l
LEFT JOIN countries cts on l.country_code = cts.code
where l.percentage > 89
ORDER BY l.percentage DESC;

/* ***********
Query:
5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
************** */
select
	cts.name, cts.surface_area, cts.population
from countries cts
where cts.surface_area < 501 AND cts.population >100000;

/* ***********
Query:
6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
************** */
select
	cts.name, cts.government_form, cts.capital, cts.life_expectancy
from countries cts
where life_expectancy > 75 AND capital >200 and government_form = 'Constitutional Monarchy';

/* ***********
Query:
7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
************** */
select
	cts.name AS "Country Name", ct.name AS "City Name", ct.district AS "District", ct.population AS "Population"
from cities ct
LEFT JOIN countries cts on ct.country_code = cts.code
where cts.name = 'Argentina' AND ct.district='Buenos Aires' AND ct.population > 500000;

/* *********** 
Query:
8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
************** */
SELECT 
	t.region,
    t.countries
FROM (Select
	region, count(*) AS countries
from countries
GROUP BY region) t
ORDER BY t.countries DESC;