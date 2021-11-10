# Fetching the api, sorting the employees by hirearchy and printing the result

import requests
import csv
import json
from requests.exceptions import HTTPError

class Employee:
    def __init__(self, name, title, manager):
        self.name = name
        self.title = title
        self.manager = manager

    def api_fetcher(self):
        try:
            api_url = "https://jsonplaceholder.typicode.com/users"
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    def sort_by_manager(self):
        api_data = self.api_fetcher()
        sorted_data = sorted(api_data, key=lambda x: x['id']) # Sorting the data by id
        return sorted_data

    def print_data(self):
        sorted_data = self.sort_by_manager()
        for data in sorted_data:
            print(data['id'], data['name'], data['username'], data['email'], data['phone'], data['website'])

    def write_to_csv(self):
        sorted_data = self.sort_by_manager()
        with open('employee.csv', 'w') as csvfile:
            fieldnames = ['id', 'name', 'username', 'email', 'phone', 'website', 'company', 'address'] # writing the HEADERS
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for data in sorted_data:
                writer.writerow(data)

    def write_to_json(self):
        sorted_data = self.sort_by_manager()
        with open('employee.json', 'w') as jsonfile:
            json.dump(sorted_data, jsonfile)


def main():
    employee = Employee('', '', '')
    employee.print_data()
    employee.write_to_csv()
    employee.write_to_json()

if __name__ == '__main__':
    main()