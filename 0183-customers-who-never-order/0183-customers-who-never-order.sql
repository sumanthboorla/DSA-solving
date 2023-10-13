# Write your MySQL query statement below

SELECT C.name as 'Customers'
FROM Customers C
LEFT JOIN Orders d ON C.id = d.CustomerId
WHERE d.CustomerId IS NULL;