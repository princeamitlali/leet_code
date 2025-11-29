# Write your MySQL query statement below
WITH CTE AS (
    select
    o.sales_id
    from Orders o
left join
Company c
on o.com_id = c.com_id
where c.name = "RED"

)
-- select * from cte
SELECT
Distinct name
from SalesPerson
 
where sales_id not in (select * from cte)


