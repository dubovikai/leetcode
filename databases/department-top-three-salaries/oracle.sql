WITH ranked_salaries AS (
    SELECT
        departmentId,
        name,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rn
    FROM Employee
)

SELECT
    department.Name AS Department,
    ranked_salaries.Name AS Employee,
    ranked_salaries.Salary
FROM ranked_salaries
JOIN Department
    ON ranked_salaries.DepartmentId = Department.Id 
WHERE ranked_salaries.rn <= 3
ORDER BY 1, 3