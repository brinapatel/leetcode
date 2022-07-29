WITH root as
(
select distinct id, 'Root' as type 
from Tree 
where p_id is null
),
leaf as 
(
    select id, 'Leaf' as type
    from Tree
    where id not in (select distinct p_id as id from Tree where p_id is not null) and p_id is not null
),
inner_node as 
(
select id, 'Inner' as type
    from Tree
    where id in (select distinct p_id from Tree where p_id is not null) and p_id is not null

)
select * from root
union
select * from leaf
union
select * from inner_node
order by id asc