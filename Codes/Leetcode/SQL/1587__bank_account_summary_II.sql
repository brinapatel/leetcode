/* Write your T-SQL query statement below */

select u.name, SUM(t.amount) as balance
from
Transactions t 
inner join Users u on u.account = t.account
group by u.name
having SUM(t.amount)>10000