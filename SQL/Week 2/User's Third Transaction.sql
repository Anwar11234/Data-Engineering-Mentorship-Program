SELECT user_id, spend, transaction_date
FROM(
  SELECT *, 
  RANK() OVER(PARTITION BY user_id ORDER BY transaction_date) as rnk
  FROM transactions
) ranked_transactions
WHERE rnk = 3