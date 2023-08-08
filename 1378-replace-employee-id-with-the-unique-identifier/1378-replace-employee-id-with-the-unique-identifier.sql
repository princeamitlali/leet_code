# Write your MySQL query statement below
select unique_id,name from employees as emp left join employeeuni as u on emp.id = u.id;
