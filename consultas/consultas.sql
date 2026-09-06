-- Show all primates
SELECT *
FROM products;

-- Show primates from a specific category
SELECT *
FROM products
WHERE category = 'Nuevo Mundo';

-- Show primates with price greater than 500
SELECT *
FROM products
WHERE price > 500;

-- Order primates by price
SELECT *
FROM products
ORDER BY price DESC;

-- Average price
SELECT AVG(price) AS average_price
FROM products;

-- Maximum price
SELECT MAX(price) AS maximum_price
FROM products;

-- Minimum price
SELECT MIN(price) AS minimum_price
FROM products;
