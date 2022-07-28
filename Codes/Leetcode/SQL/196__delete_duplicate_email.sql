WITH duplicate as (
select id, email, ROW_NUMBER() OVER (PARTITION BY email order by id) rn
    from Person
)
delete from 
Person   
where id in (
select id from duplicate where rn>1
)