# Write your MySQL query statement below

Select p.firstName, p.lastName, a.city, a.state
From person p Left Join address a 
on p.personId = a.personId