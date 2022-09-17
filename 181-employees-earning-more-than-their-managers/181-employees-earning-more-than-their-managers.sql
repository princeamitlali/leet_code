# Write your MySQL query statement below

select t1.name as Employee from Employee  as t1 where t1.salary > (select salary from employee where id = t1.managerId)
