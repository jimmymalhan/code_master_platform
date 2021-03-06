# There are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and 
# print each name on a new line.

## Input ##
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

## Output ##
# Berry
# Harry

dict = {}
for _ in range(int(input())):
    name = str(input())
    grade = float(input())
    dict[name] = grade
values = dict.values()

second = sorted(list(set(values)))[1]
second_lowest = []

for key, value in dict.items():
    if value == second:
        second_lowest.append(key)

second_lowest.sort()

for name in second_lowest:
    print(name)

dict = {} # empty dictionary
for _ in range(int(input())): # range of number of students
    name = input() # accepting the name of the students
    grade = float(input()) # accepting accepting the grade of the students
    dict[name] = grade # assigning name as KEY and grade as VALUE for the dict
values = dict.values() #obtaining the values of dictionary

second = sorted(list(set(values)))[1] # removing duplicate grades by using set data type, changing it to list, sorting in ascending order 
#and taking the second lowest grade
second_lowest=[] #declaring an empty list for storing the name of the sudents who got the second lowest grade

for key, value in dict.items(): #going through the name and grade of each students by using items()= method of dictonary
    if value==second: # checking whether the grade is equal to the second lowest grade
        second_lowest.append(key) #if yes, append it to the second lowest grade

second_lowest.sort() #sorting the name of students in ascending order

for name in second_lowest: #going through the name of each students who got the second lowest grade
    print(name) # printing each name of students in seperate line
