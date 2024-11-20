-- approach 1
WITH visits AS (
    SELECT *,
    LEAD(id, 1) OVER(ORDER BY id) AS next_id,
    LEAD(id, 2) OVER(ORDER BY id) AS second_next_id,
    LEAD(id, 1) OVER(ORDER BY id) AS prev_id,
    LEAD(id, 2) OVER(ORDER BY id) AS second_prev_id
    FROM Stadium
    WHERE people >= 100
)

SELECT id, visit_date, people
FROM visits
WHERE (next_id - id = 1 AND id - prev_id = 1)
OR (second_next_id - next_id = 1 AND next_id - id = 1)
OR (id - prev_id = 1 AND prev_id - second_prev_id = 1)

-- aproach 2
with ranked_visits AS (
    SELECT id, visit_date, people, (id - rnk) AS group_id
    FROM (
        SELECT id,visit_date, people, rank() OVER(ORDER BY id) AS rnk
        FROM Stadium
        WHERE people >= 100
    ) subquery
)

SELECT id, visit_date, people
FROM ranked_visits
WHERE group_id in (
    SELECT group_id 
    FROM ranked_visits 
    GROUP BY group_id 
    HAVING COUNT(*) >= 3
)