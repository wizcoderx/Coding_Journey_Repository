--https://www.hackerrank.com/challenges/earnings-of-employees

SELECT MAX(SALARY*MONTHS), COUNT(*)
FROM EMPLOYEE
WHERE (SALARY*MONTHS) = (SELECT MAX(SALARY*MONTHS)
                         FROM EMPLOYEE);

                        -- This query selects the employee ID, first name, last name, and department name
                        -- from the employees and departments tables. It performs an inner join on the
                        -- department_id field to match employees with their respective departments.
                        -- The results are ordered by the employee's last name in ascending order.