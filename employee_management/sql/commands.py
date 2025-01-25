
INSERT_EMPLOYEE = """
INSERT INTO employees (name, email, department, salary)
VALUES (%s, %s, %s, %s)
"""


UPDATE_EMPLOYEE = """
UPDATE employees
SET {fields}
WHERE id = %s
"""


DELETE_EMPLOYEE = """
DELETE FROM employees
WHERE id = %s
"""


GET_ALL_EMPLOYEES = """
SELECT * FROM employees
ORDER BY id
"""


AVG_SALARY_BY_DEPARTMENT = """
SELECT 
    department,
    ROUND(AVG(salary), 2) AS average_salary,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department
"""
