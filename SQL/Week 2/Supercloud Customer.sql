SELECT customer_id
FROM customer_contracts c 
JOIN products p
ON c.product_id = p.product_id
group by customer_id
HAVING COUNT(DISTINCT product_category) = (SELECT count(DISTINCT product_category) from products)