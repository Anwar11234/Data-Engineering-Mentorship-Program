SELECT 
    u.user_id as buyer_id,
    join_date, 
    COUNT(o.order_id) AS orders_in_2019
FROM 
    Users u
    LEFT JOIN Orders o
    ON u.user_id = o.buyer_id AND EXTRACT(YEAR FROM order_date) = 2019
GROUP BY u.user_id, join_date