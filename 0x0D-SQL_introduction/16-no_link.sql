-- This script lists all records of the table second_table of the database
-- Doesn't list rows without a name value
-- Display the score and the name
-- Records are listed in descending order according to score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
