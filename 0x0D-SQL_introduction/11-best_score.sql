-- Script that lists all records with a score >= 10 in the table
-- second_table of the databasse hbtn_0c_0 in the MySQL server
-- Display score and the name
-- Records are ordered by score
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC
