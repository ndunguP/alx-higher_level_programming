-- Import in hbrn_0c_0 database a table dump. This script displays
-- the average temperature by city ordered by temperature
SELECT
    city, AVG(value) AS avg_temp
FROM
    temperatures
GROUP BY
    city
ORDER BY
    avg_temp DESC
