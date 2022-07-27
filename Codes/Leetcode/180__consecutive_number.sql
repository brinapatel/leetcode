select distinct l1.num as ConsecutiveNums 
from
Logs l1,
Logs l2,
Logs l3 
where l1.id = (l2.id+1) and
 l1.id = (l3.id+2) and l1.num = l2.num
 and l2.num = l3.num

 ---------------------------------------------------


WITH cte_1 AS 
(SELECT num, 
        LEAD(num) OVER(order by id) as next,
        LAG(num) OVER(order by id) as prev
FROM Logs)
SELECT DISTINCT num AS ConsecutiveNums 
FROM cte_1 WHERE
num = next and next = prev