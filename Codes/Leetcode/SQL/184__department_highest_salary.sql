select Department, Employee, Salary from
(select d.name as Department,
e.name as Employee, 
e.salary,
DENSE_RANK() over(partition by d.id ORDER BY e.salary desc) as rnk
from  Employee e inner join Department d on e.departmentId = d.id
) t 
where t.rnk = 1

--------------------------------------------------------------------

WITH max_sal as (select max(salary) sal, departmentId
from 
Employee 
group by departmentId)
select d.name as Department, e.name as Employee, m.sal as Salary
from Employee e 
inner join Department d on e.departmentId = d.id  
inner join max_sal m on m.departmentId = e.departmentId and e.salary = m.sal