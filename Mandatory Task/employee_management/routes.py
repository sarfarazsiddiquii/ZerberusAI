from flask import request, jsonify
from db import get_db_connection
from sql.commands import INSERT_EMPLOYEE, UPDATE_EMPLOYEE, DELETE_EMPLOYEE, GET_ALL_EMPLOYEES, AVG_SALARY_BY_DEPARTMENT
from utils import validate_employee_data

def setup_routes(app):
    @app.route('/employee', methods=['POST'])
    def add_employee():
        try:
            data = request.json
            validate_employee_data(data['name'], data['email'], data['department'], data['salary'])

            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute(INSERT_EMPLOYEE, (data['name'], data['email'], data['department'], data['salary']))
            
            connection.commit()
            employee_id = cursor.lastrowid
            connection.close()
            
            return jsonify({"id": employee_id, "message": "Employee created successfully"}), 201
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/employees', methods=['GET'])
    def get_all_employees():
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(GET_ALL_EMPLOYEES)
            employees = cursor.fetchall()

            connection.close()

            return jsonify(employees), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/employees/avg-salary', methods=['GET'])
    def get_avg_salary_by_department():
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute(AVG_SALARY_BY_DEPARTMENT)
            department_stats = cursor.fetchall()

            connection.close()

            return jsonify(department_stats), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/employee/<int:employee_id>', methods=['PUT'])
    def update_employee(employee_id):
        try:
            data = request.json

            connection = get_db_connection()
            cursor = connection.cursor()

            # Fetch existing employee data
            cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
            existing_employee = cursor.fetchone()

            if not existing_employee:
                return jsonify({"error": "Employee not found"}), 404

            # Update only the provided fields
            updated_data = {
                "name": data.get('name', existing_employee['name']),
                "email": data.get('email', existing_employee['email']),
                "department": data.get('department', existing_employee['department']),
                "salary": data.get('salary', existing_employee['salary'])
            }

            validate_employee_data(updated_data['name'], updated_data['email'], updated_data['department'], updated_data['salary'])

            cursor.execute(UPDATE_EMPLOYEE, (updated_data['name'], updated_data['email'], updated_data['department'], updated_data['salary'], employee_id))
            
            connection.commit()
            connection.close()
            
            return jsonify({"message": "Employee updated successfully"}), 200
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/employee/<int:employee_id>', methods=['DELETE'])
    def delete_employee(employee_id):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute(DELETE_EMPLOYEE, (employee_id,))
            
            connection.commit()
            connection.close()
            
            return jsonify({"message": "Employee deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
