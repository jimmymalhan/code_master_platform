# There are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and 
# print each name on a new line.

# Input
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

# Output
# Berry
# Harry

dict = {} # empty dictionary
for _ in range(int(input())): # range of number of students
    name = input() # accepting the name of the students
    grade = float(input()) # accepting accepting the grade of the students
    dict[name] = grade # assigning name as key and grade as value for the dict
values = dict.values() #obtaining the values of dictionary 
second = sorted(list(set(values)))[1] # removing duplicate grades by using set data type, changing it to list, sorting in ascending order and taking the second lowest grade
second_lowest=[] #declaring an empty list for storing the name of the sudents who got the second lowest grade
for key, value in dict.items(): #going through the name and grade of each students by using items()= method of dictonary
    if value==second: # checking whether the grade is equal to the seond lowest grade
        second_lowest.append(key) #if yes, append it to the second lowest grade
second_lowest.sort() #sorting the name of students in ascending order
for name in second_lowest: #going through the name of each students who got the second lowest grade
    print(name) # printing each name of students in seperate line

#concise
a = [[input(), float(input())] for i in range(int(input()))] # returns the k,v in dict
s = sorted(set([x[1] for x in a])) # returns the sorted values from dict
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print(name)