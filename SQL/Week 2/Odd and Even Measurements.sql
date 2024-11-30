WITH ranked_measurements AS(
  SELECT *, row_number() OVER(PARTITION by measurement_time::DATE ORDER by measurement_time) AS rn
  FROM measurements
)

SELECT measurement_time::DATE as measurement_day, 
sum(case when rn % 2 != 0 then measurement_value else 0 end) as odd_sum,
sum(case when rn % 2 = 0 then measurement_value else 0 end) as even_sum
FROM ranked_measurements
group by measurement_time::DATE
order by measurement_day