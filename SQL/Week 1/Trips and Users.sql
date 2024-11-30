SELECT request_at AS Day, 
ROUND(SUM(CASE WHEN status != 'completed' THEN 1.00 ELSE 0.00 END) / COUNT(*), 2) AS "Cancellation Rate"
FROM Trips t
JOIN Users c
ON t.client_id = c.users_id
JOIN Users d
ON t.driver_id = d.users_id
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03' AND c.banned = 'No' AND d.banned = 'No'
GROUP BY request_at