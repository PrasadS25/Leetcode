SELECT ROUND(SUM(CASE WHEN DATEDIFF(a2.event_date,a1.event_date) = 1 THEN 1 ELSE 0 END)/COUNT(DISTINCT a1.player_id),2) AS fraction
FROM activity a1, activity a2
WHERE (a1.player_id, a1.event_date) IN (SELECT player_id,MIN(event_date) FROM activity GROUP BY player_id) AND a1.player_id=a2.player_id;