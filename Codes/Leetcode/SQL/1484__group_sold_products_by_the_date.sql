/* Write your T-SQL query statement below */

select sell_date, count(distinct product) num_sold, string_agg(product,',') WITHIN GROUP (order by product asc) as products
from 
(select distinct * from Activities ) t
group by sell_date