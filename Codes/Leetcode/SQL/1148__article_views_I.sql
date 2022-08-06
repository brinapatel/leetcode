select distinct v1.author_id as id from 
Views v1, Views v2
where v1.author_id = v2.viewer_id
and v1.article_id = v2.article_id
order by v1.author_id asc