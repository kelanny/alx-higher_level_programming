-- List number of records with the same score.
-- Table: second_table
-- Database: hbtn_0c_0
-- Server: MySQL

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC, score;
