CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) 
RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    WITH ranked_salaries AS (
        SELECT 
            e.salary, 
            DENSE_RANK() OVER (ORDER BY e.salary DESC) AS rnk
        FROM Employee e
    )
    SELECT DISTINCT rs.salary 
    FROM ranked_salaries rs
    WHERE rs.rnk = N
  );
END;
$$ LANGUAGE plpgsql;
