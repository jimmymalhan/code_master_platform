#######################################
# Parse API in JSON format
#######################################
import time
import requests
import json
from requests.exceptions import HTTPError
# Read the file and print the results in json format

# def Solution():
#     file = open("input.json", "rt")
#     print(file.read())

# if __name__ == "__main__":
#     Solution()

#######################################
# Sanity checks of the website

# def Solution():
#     response=requests.get('https://my-json-server.typicode.com/typicode/demo/db')
#     print(response.status_code) # check the status code of the website response
#     print(response.raise_for_status()) # raises the error for status
#     print(response.text) # prints the output of the website
#     print(response.url) # prints the url of the website

#     jsonResponse = response.json() # convert the response to json
#     print(jsonResponse)

# if __name__ == "__main__":
#     Solution()

#######################################
# fetch the data and add custom headers

# Brute force

# O(n) time - looping through until gets it
# O(n) time - extra storage of the vars where n is length of elements

# response=requests.get('https://my-json-server.typicode.com/typicode/demo/db')
# try:
#     jsonResponse = response.json() # convert json response
#     response.raise_for_status()
#     result1 = jsonResponse["posts"][1] # posts is the first block | HEADER | [1] fetching key and value for at index 1
#     # print(result1)
#     actual_value = {}

#     for key in result1:
#         value = result1[key] # checking the VALUE # extra storage
#         if value == "Post 2": # if the VALUE is "Post 2"
#             actual_value["posts_title"] = "Post 2" # adding KEY(custom header)- "posts_title"
    
#     result2 = jsonResponse["profile"] # profile is the third block | HEADER
#     for key in result2:
#         value = result2[key] # checking the VALUE 

#         if value == "typicode":
#             actual_value["profile_name"] = "typicode" # adding KEY(custom header)- "profile_name"

#     with open('output.json', 'w') as convert_file:
#         convert_file.write(json.dumps(actual_value)) # writing output to the file

# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')
# except Exception as err:
#     print(f'Other error occurred: {err.__str__()}')

# method 3

# O(n) time - looping through until gets it
# O(1) time - constant variables

def Solution():
    try:
        response = requests.get('https://my-json-server.typicode.com/typicode/demo/db')
        jsonResponse = response.json()

        actual_value = {}
        index = 0

        result1 = jsonResponse["posts"][1]
        for key, value in result1.items():
            
            if value == "Post 2":
                actual_value["posts_title"] = "Post 2"
                index += 1
            
        result2 = jsonResponse["profile"]
        for key, value in result2.items():
            
            if value != "typicode":
                break

            elif value == "typicode":
                actual_value["profile_name"] = "typicode"
                index += 1

        with open('output.json', 'wt') as convert_file:
            convert_file.write(json.dumps(actual_value))

# check the time to take to run this code
        start_time = time.time()
        print("--- %s seconds ---" % (time.time() - start_time))

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err.__str__()}')

if __name__ == "__main__":
    Solution()