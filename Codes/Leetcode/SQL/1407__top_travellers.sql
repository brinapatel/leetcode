with dataset as (
select u.name, sum(ISNULL(r.distance,0)) OVER(Partition by u.id) as travelled_distance
from
Users u left join Rides r on r.user_id = u.id
)
select distinct * from dataset
order by travelled_distance desc, name asc