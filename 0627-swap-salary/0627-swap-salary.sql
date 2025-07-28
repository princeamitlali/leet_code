# Write your MySQL query statement below
update salary
    set sex = IF (sex = 'f', 'm', 'f')
