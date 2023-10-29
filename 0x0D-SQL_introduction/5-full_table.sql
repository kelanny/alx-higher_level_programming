-- Prints full description of a table first_table in hbtn_0c_0

USE information_schema;

SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY, COLUMN_COMMENT
FROM COLUMNS
WHERE TABLE_SCHEMA ='hbtn_0c_0' AND TABLE_NAME = 'first_table';
