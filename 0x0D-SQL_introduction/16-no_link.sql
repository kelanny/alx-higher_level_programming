-- Lists all records of the table second_table of hbtn_0c_0 db.
-- Don't list rows without a name value.
-- Result displays the score and name respectively
-- Records should be listed by descending score.
-- Db name will be passed as an argument.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
