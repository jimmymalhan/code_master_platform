# Fetching the api, sorting the employees by title, and printing the results

import requests
import operator
import csv
import http
import json

class Employee:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary
    
    def api_call(self):
        response = requests.get('https://randomuser.me/api/?results=10')
        return response.json()

    def sort_employees(self):
        employees = self.api_call()
        sorted_employees = sorted(employees['results'], key=operator.itemgetter('name'))
        return sorted_employees

    def print_employees(self):
        sorted_employees = self.sort_employees()
        for employee in sorted_employees:
            print(employee['name']['first'], employee['name']['last'], employee['title'], employee['location']['city'], employee['location']['state'], employee['email'], employee['phone'])
    
def main():
    employee = Employee('', '', '')
    employee.print_employees()

if __name__ == '__main__':
    main()