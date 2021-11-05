# Fetching the api, sorting the employees by hirearchy and printing the result

import requests
import csv
from requests.exceptions import HTTPError

class Employee:
    def __init__(self, name, salary, age, department, manager):
        self.name = name
        self.salary = salary
        self.age = age
        self.department = department
        self.manager = manager

    def api_fetch(self):
        try:
            response = requests.get('http://dummy.restapiexample.com/api/v1/employees')
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    def sort_by_hirearchy(self):
        data = self.api_fetch()
        sorted_data = sorted(data, key=lambda x: x['employee_department']) # Sorting the data by department
        return sorted_data

    def print_result(self):
        sorted_data = self.sort_by_hirearchy()
        for employee in sorted_data:
            print(f'{employee["employee_name"]} is in {employee["employee_department"]} department and manages {employee["employee_manager_name"]}')

    def write_to_csv(self):
        sorted_data = self.sort_by_hirearchy()
        with open('employees.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Salary', 'Age', 'Department', 'Manager'])
            for employee in sorted_data:
                csv_writer.writerow([employee['employee_name'], employee['employee_salary'], employee['employee_age'], employee['employee_department'], employee['employee_manager_name']])

    def read_from_csv(self):
        with open('employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)

def main():
    employee = Employee('', '', '', '', '')
    employee.write_to_csv()
    employee.read_from_csv()

if __name__ == '__main__':
    main()