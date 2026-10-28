USE sakila;

SELECT COUNT(*)
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';

SELECT COUNT(DISTINCT name)
FROM category;

SELECT SUM(amount)
FROM payment;

SELECT COUNT(DISTINCT film_id) total_films
FROM film;

SELECT AVG(amount) a, SUM(amount) s
FROM payment;

SELECT customer_id c, AVG(amount) s
FROM payment
GROUP BY customer_id;

SELECT customer_id, COUNT(*) AS rental_count
FROM rental
GROUP BY customer_id
ORDER BY rental_count DESC;

SELECT customer_id, COUNT(*) rental_count
FROM rental
GROUP BY customer_id
HAVING rental_count > 5;

SELECT r.customer_id, COUNT(*) AS rental_count, SUM(p.amount) AS total_spent
FROM rental r
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY r.customer_id
HAVING rental_count > 5 AND total_spent > 100;

