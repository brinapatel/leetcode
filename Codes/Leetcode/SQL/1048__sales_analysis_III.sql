WITH not_elligible as (
    select product_id from Sales where sale_date not between '2019-01-01' and '2019-03-31'
    )
    select distinct s.product_id, product_name
    from
    Sales s 
    inner join Product p on p.product_id = s.product_id
    left join not_elligible e on e.product_id = s.product_id
    where e.product_id is null