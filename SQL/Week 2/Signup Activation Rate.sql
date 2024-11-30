SELECT round(count(t.email_id)::DECIMAL /  count(user_id), 2) as confirm_rate
FROM emails e
LEFT JOIN texts t 
ON e.email_id = t.email_id
AND signup_action = 'Confirmed'