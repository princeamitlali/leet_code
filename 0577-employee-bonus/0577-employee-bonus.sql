/* Write your T-SQL query statement below */
select emp.name,bonus 
from bonus 
right join employee emp 
on emp.empid = bonus.empid 
where  bonus <1000 or bonus is null