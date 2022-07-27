CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (

        select top 1 n.salary from 
        (select salary, DENSE_RANK() OVER(order by salary desc) as rnk from Employee) n 
        where n.rnk = @N
        
    );
END