WITH cnt_table as (select customer_number, count(order_number) as cnt
from Orders
group by customer_number)

select customer_number from 
cnt_table t where t.cnt = (select max(cnt) from cnt_table)

-------------------------------------------------------------------------
--The second approach is slower
-------------------------------------------------------------------------
select top 1 customer_number 
from
Orders
group by customer_number
order by count(order_number) desc