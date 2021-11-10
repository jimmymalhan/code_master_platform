# Assume there is a REST API available at "http://www.linkedin.corp/api" for accessing employee information. The employee information endpoint is "/employee/<id>". Each employee record you retrieve will be a JSON object with the following keys:

#   - 'name'  refers to a String that contains the employee's first and last name

#   - 'title' refers to a String that contains the employee's job title

#   - 'reports' refers to an Array of Strings containing the IDs of the employee's direct reports


# Sample JSON API Response:

# # GET /employee/A123456789
# {
#  "name": "Flynn Mackie",
#  "title": "Senior VP of Engineering",
#  "reports": ["A123456793", "A1234567898"]
# }
# Write a function that will take an employee ID and print out the entire hierarchy, rooted at that employee, and including all employees under that employee.

# For example, suppose that Flynn Mackie's employee id is 'A123456789' and his only direct reports are Wesley Thomas and Nina Chiswick. If you provide 'A123456789' as input to your function, you will see the sample output below.


# -----------Begin Sample Output--------------
# Flynn Mackie - Senior VP of Engineering
#   Wesley Thomas - VP of Design
#     Randall Cosmo - Director of Design
#       Brenda Plager - Senior Designer
#   Nina Chiswick - VP of Engineering
#     Tommy Quinn - Director of Engineering
#       Jake Farmer - Frontend Manager
#         Liam Freeman - Junior Software Engineer
#       Sheila Dunbar - Backend Manager
#         Peter Young - Senior Code Cowboy
# -----------End Sample Output--------------

import requests
from requests.exceptions import HTTPError

class Employee:
    def __init__(self, name, title, reports):
        self.name = name
        self.title = title
        self.reports = reports

    def api_fetcher(self, id):
        try:
            response = requests.get('http://www.linkedin.corp/api/employee/{}'.format(id))
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return response.json()

    def print_hierarchy(self, id):
        employee = self.api_fetcher(id)
        print(employee['name'] + ' - ' + employee['title'])
        for report in employee['reports']:
            self.print_hierarchy(report)

def main():
    employee = Employee('', '', [])
    employee.print_hierarchy('A123456789')
    employee.print_hierarchy_recursive('A123456789')

if __name__ == '__main__':
    main()