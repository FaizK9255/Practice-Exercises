USE sakila;

-- Aggregate: one result for the whole table
SELECT AVG(rental_rate) FROM film;

-- Scalar: one result for every row
SELECT title, rental_rate, ROUND(rental_rate) AS rounded_rate
FROM film;

-- AVG returns one record
-- ROUND returns 10 rows
-- ROUND is a scalar function because 