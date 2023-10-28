0x0D. SQL - Introduction
SQL
MySQL
 By: Guillaume
 Weight: 1
 Project over - took place from Oct 17, 2023 6:00 AM to Oct 18, 2023 6:00 AM

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions


TASK: 0. List databases
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all databases of your MySQL server.

TASK: 1. Create a database
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that creates the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements


TASK: 2. Delete a database
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that deletes the database hbtn_0c_0 in your MySQL server.

If the database hbtn_0c_0 doesn’t exist, your script should not fail
You are not allowed to use the SELECT or SHOW statements


TASK: 3. List tables
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)


TASK: 4. First table
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that creates a table called first_table in the current database in your MySQL server.

first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first_table already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements


TASK: 5. Full description
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements


TASK: 6. List all in table
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

All fields should be printed
The database name will be passed as an argument of the mysql command


TASK: 7. First add
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

New row:
id = 89
name = Best School
The database name will be passed as an argument of the mysql command


TASK: 8. Count 89
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

The database name will be passed as an argument of the mysql command

TASK: 9. Full creation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

second_table description:
id INT
name VARCHAR(256)
score INT
The database name will be passed as an argument to the mysql command
If the table second_table already exists, your script should not fail
You are not allowed to use the SELECT and SHOW statements
Your script should create these records:
id = 1, name = “John”, score = 10
id = 2, name = “Alex”, score = 3
id = 3, name = “Bob”, score = 14
id = 4, name = “George”, score = 8


 TASK: 10. List by best
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

Results should display both the score and the name (in this order)
Records should be ordered by score (top first)
The database name will be passed as an argument of the mysql command

`
