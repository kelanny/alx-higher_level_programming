-- Creates the database hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Connect to the database
USE hbtn_0d_usa;

-- Create table "states"
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
