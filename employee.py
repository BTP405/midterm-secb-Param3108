"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.
"""

class Employee:
    """
    Class representing an employee in the company.

    Attributes:
        name (str): The name of the employee.
        emp_id (str): The employee ID.
        role (str): The role of the employee.
        salary (float): The salary of the employee.
    """

    def __init__(self, name, emp_id, role, salary):
        """
        Initialize an Employee object.

        Args:
            name (str): The name of the employee.
            emp_id (str): The employee ID.
            role (str): The role of the employee.
            salary (float): The salary of the employee.
        """
        pass
self.name = name
        self.emp_id = emp_id
        self.role = role
        self.salary = salary


employee1 = Employee("Param katrodia", "1234", "Cyber Security Specialist", 75000)
print(employee1.name)  
print(employee1.emp_id)
print(employee1.role)  
print(employee1.salary)  
