# Write your MySQL query statement below

Select firstName, lastName, city, state
From person p Left Join address a on p.personId = a.personId