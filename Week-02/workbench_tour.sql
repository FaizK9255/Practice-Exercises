/* 
Ex1C – Workbench Readiness Check 
Name: Faiz Khan Date: 10/20/2026 
Q1: It shows host name root, and the port is  localhost:3306
Q2: You would click file > new query tab
Q3: 1 - navigator 2 - Information 3 - Query Editor 4 - Output 5 - SQL Additions
Q4: root - 3306 - 8.0.46
Q5: Server Status and Client Connections
Q6: the data type is small int, a whole number integer. PK - Primary Key, AI - Auto Increment 
Q7: Colums - actor_id, film_id, last_update. There are two foereign keys and I believe that they point to the actor and film tables
Q8: It opened up a new query selecting from the sakila film actor table. It oututs a table
Q9: In the action output I  can see that it returned 200 rows
Q10: Eveything succeeded, except line 17 had error code 1146
Q11: It only inputs the command of that line, could be useful to isolate commands
Q12: AKROYD
Q13: Three
Q14: First_Name is  a VARCHAR and max length is 11
*/ 

USE sakila;
select * from actor;
SELECT * FROM sakila.film;
SELECT * FROM actor;
