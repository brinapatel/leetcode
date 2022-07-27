select email 
from Person
group by email
having count(id) > 1

select distinct email from 
(select email, ROW_NUMBER() OVER(PARTITION BY email order by id) rnk
from Person) t
where t.rnk > 1


