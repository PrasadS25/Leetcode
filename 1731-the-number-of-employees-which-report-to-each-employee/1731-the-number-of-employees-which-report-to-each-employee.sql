SELECT e.reports_to as employee_id, 
        names.name,
        COUNT(*) AS reports_count,
        ROUND(AVG(age),0) AS average_age
FROM employees e JOIN (SELECT employee_id, name FROM employees) as names
ON names.employee_id = e.reports_to
GROUP BY (e.reports_to)
ORDER BY (e.reports_to);