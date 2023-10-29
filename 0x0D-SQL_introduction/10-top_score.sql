-- List all records of the table second_table in hbtn_0c_0 db.
-- Results should display both the score and the name respectively.
-- Records should be ordered by score (top first).
-- Db name will be passed as an argument of mysql command.

SELECT score, name
FROM second_table
ORDER BY score DESC;
