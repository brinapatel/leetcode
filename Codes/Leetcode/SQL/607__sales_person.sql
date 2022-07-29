WITH red_orders AS
(
select sales_id from 
    Orders o inner join Company c 
    on o.com_id = c.com_id
    where c.name = 'Red'
)
select s.name
from
SalesPerson s
where
s.sales_id not in (
select * from red_orders
)