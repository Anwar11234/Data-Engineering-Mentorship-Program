SELECT user_id, tweet_date, 
ROUND(AVG(tweet_count) 
OVER(PARTITION BY user_id ORDER BY tweet_date rows between 2 preceding and current row),2) as rolling_avg_3d 
FROM tweets