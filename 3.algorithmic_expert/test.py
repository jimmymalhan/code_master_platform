# Fetching the api, sorting the results by employee title
# and printing the results to the console.
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

    def api(self):
        url = "https://randomuser.me/api/?results=10"
        response = requests.get(url)
        data = response.json()
        employees = data["results"]
        employees_dict = {}
        for employee in employees:
            name = employee["name"]
            title = employee["name"]["title"]
            salary = employee["name"]["salary"]
            employees_dict[name] = Employee(name, title, salary)
        sorted_employees = sorted(employees_dict.items(), key=operator.itemgetter(1), reverse=True)
        for employee in sorted_employees:
            print(employee[0], employee[1].title, employee[1].salary)
        return sorted_employees

    def write_to_csv(self, sorted_employees):
        with open("employees.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Name", "Title", "Salary"])
            for employee in sorted_employees:
                writer.writerow([employee[0], employee[1].title, employee[1].salary])

def main():
    employee = Employee("", "", "")
    employee.api()
    employee.write_to_csv(employee.api())

if __name__ == "__main__":
    main()