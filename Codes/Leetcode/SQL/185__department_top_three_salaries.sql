WITH dataset as (
select e.name Employee, d.name Department, e.salary Salary, DENSE_RANK() OVER(Partition by d.id order by e.salary desc) rnk
from Employee e inner join Department d on e.departmentId = d.id
    )
    select Department, Employee, Salary from dataset
    where rnk<=3