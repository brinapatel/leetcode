/* Write your T-SQL query statement below */

select * from patients where conditions like 'DIAB1%' or conditions like '% DIAB1%'