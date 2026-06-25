# SQL Notes

## Day 1-SELECT Basics
SELECT helps choose which columns to return from a table
FROM chooses which table to take from
Example: SELECT name, population FROM world

Filtering to specific rows: 
WHERE name='Ireland'

Matching an item against a list of options:
WHERE name IN ('Ireland', 'France', 'Germany')

Selecting a range of values inclusive:
WHERE population BETWEEN 5000000 AND 6000000

Identifying patterns matches based on certain characters:
WHERE name LIKE 'Ir%'

## DAY 2-SELECT from world
Selecting data based on exclusive factors:
WHERE population > 500000 OR area > 300000

Selecting data based on exclusivity (Specific for MySQL):
WHERE population > 1000000 XOR area > 250000

Rounding numerical outputs:
SELECT name,
       ROUND(gdp/population, 2)
   FROM world

Finding the number of characters in a string:
WHERE LENGTH(name)= 10

Isolating the first/last character(s) in a string:
WHERE LEFT(name,1)= 'A'
WHERE RIGHT(capital,2)= 'in'

Indicating that objects are not equal:
WHERE name<>capital

Excluding rows from results that match a pattern:
AND name NOT LIKE '%z%'
