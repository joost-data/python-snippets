-- Select all rows
SELECT * FROM table_name;

-- Filter rows
SELECT * FROM table_name
WHERE column_name = 'value';

-- Aggregate
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;

