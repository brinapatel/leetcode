select w2.id from 
Weather w1 , Weather w2
where datediff(day, w1.recordDate, w2.recordDate) = 1
and w2.temperature > w1.temperature

