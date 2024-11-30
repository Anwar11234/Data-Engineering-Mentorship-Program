WITH cte AS (
  SELECT age_bucket, 
  SUM(CASE WHEN activity_type = 'open' then time_spent else 0.00 END) as open_time,
  SUM(CASE WHEN activity_type = 'send' then time_spent else 0.00 END) as send_time
  FROM activities a
  JOIN age_breakdown ab 
  ON a.user_id = ab.user_id
  GROUP BY age_bucket
)

SELECT 
age_bucket, 
ROUND(send_time * 100.00 / (open_time + send_time),2) as send_perc,
ROUND(open_time * 100.00 / (open_time + send_time), 2) as open_perc
from cte