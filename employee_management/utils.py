import re

def validate_employee_data(name, email, department, salary):
    if not name or len(name) < 2:
        raise ValueError("Name must be at least 2 characters long")
    
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format")
    
    if not department or len(department) < 2:
        raise ValueError("Department must be at least 2 characters long")
    
    if not salary or salary < 0:
        raise ValueError("Salary must be a positive number")
