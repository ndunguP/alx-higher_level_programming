-- This script create a table in the current database of the MySQL server
-- if it doesn't exist
-- Not allowed to use the SELECT or SHOW statements
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(255)
);
