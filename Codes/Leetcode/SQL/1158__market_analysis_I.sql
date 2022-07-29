WITH orders_2019 as(
select distinct u.user_id as buyer_id, u.join_date, COUNT(o.order_id) OVER(Partition by o.buyer_id) orders_in_2019
from 
Users u 
inner join Orders o on u.user_id = o.buyer_id
where year(o.order_date) = '2019'
)
select u.user_id as buyer_id, u.join_date, ISNULL(o.orders_in_2019,0) as orders_in_2019
from 
Users u 
left join orders_2019 o on u.user_id = o.buyer_id