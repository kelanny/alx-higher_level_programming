-- Displays the average temperature (Fahrenheit)
-- By city
-- Ordered by temperature (descending)

SELECT city, AVG(value) AS ave_temp_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY ave_temp_fahrenheit;
