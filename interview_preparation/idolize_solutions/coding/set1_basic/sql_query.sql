--Given a table `Employees` with columns `EmployeeID`, `Name`, and `Salary`, write an SQL query to find the second-highest salary.

SELECT MAX(Salary) AS SecondHighestSalary
FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees);