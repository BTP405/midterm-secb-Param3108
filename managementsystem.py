"""
Module: management_system.py

This module contains classes for managing employees, projects, and tasks in a fictional company.

Classes:
    - Employee: Represents an employee in the company.
    - Project: Represents a project in the company.
    - Task: Represents a task in the company.
    - ManagementSystem: Provides functionality to manage employees, projects, and tasks.
"""

class ManagementSystem:
    """
    Class representing a management system for employees, projects, and tasks in the company.

    Attributes:
        employees (list): List of employees in the system.
        projects (list): List of projects in the system.
        tasks (list): List of tasks in the system.
    """

    def __init__(self):
        """
        Initialize a ManagementSystem object.
        """
        self.employees = []
        self.projects = []
        self.tasks = []

    def add_employee(self, employee):
        """
        Add an employee to the management system.

        Args:
            employee (Employee): The employee to be added.
        """
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        """
        Remove an employee from the management system.

        Args:
            emp_id (str): The ID of the employee to be removed.
        """
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return
        # Raise ValueError if employee is not found
        raise ValueError(f"Employee with ID {emp_id} not found.")

    def add_project(self, project):
        """
        Add a project to the management system.

        Args:
            project (Project): The project to be added.
        """
        self.projects.append(project)

    def add_task(self, task):
        """
        Add a task to the management system.

        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)

    def assign_employee_to_project(self, emp_id, project_id):
        """
        Assign an employee to a project.

        Args:
            emp_id (str): The ID of the employee to be assigned.
            project_id (str): The ID of the project to which the employee will be assigned.
        
        Raises:
            ValueError: If employee or project is not found.
        """
        employee_found = False
        project_found = False

        # Check if employee exists
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee_found = True
                break

        # Check if project exists
        for project in self.projects:
            if project.project_id == project_id:
                project_found = True
                break

        # Raise ValueError if employee or project is not found
        if not employee_found or not project_found:
            raise ValueError("Employee or project not found.")

        # Assign employee to project
        for project in self.projects:
            if project.project_id == project_id:
                project.assign_employee(employee)
                break
