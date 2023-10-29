-- Lists all records with a score >= 10 displaying name and score respectively.
-- 0rdered by score (top first)
-- Table: second_table
-- Database: hbtn_0c_0
-- Server: MySQL

SELECT score, name
FROM second_table
WHERE score >=10
ORDER BY score DESC;
