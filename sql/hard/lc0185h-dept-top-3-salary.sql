WITH
SalaryRanked AS (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rnk
    FROM Employee
)
SELECT
    d.name AS department,
    s.name AS employee,
    s.salary
FROM SalaryRanked s
INNER JOIN Department d ON s.departmentId = d.id
WHERE rnk <= 3
ORDER BY s.salary DESC
;