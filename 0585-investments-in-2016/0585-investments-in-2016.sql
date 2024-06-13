SELECT ROUND(SUM(tiv_2016),2) as tiv_2016
FROM insurance i 
JOIN (SELECT pid,COUNT(*) OVER(PARTITION BY tiv_2015) as tiv15
FROM insurance) AS CTE1 ON Cte1.pid = i.pid
JOIN (SELECT pid, COUNT(*) OVER(PARTITION BY lat,lon) as ll
FROM insurance) AS cte2 ON cte2.pid = i.pid
WHERE cte1.tiv15>1 AND cte2.ll=1