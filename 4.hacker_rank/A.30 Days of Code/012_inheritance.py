# Grading Scale 
# O | 90 <= a <= 100
# E | 80 <= a < 90
# A | 70 <= a < 80
# P | 55 <= a < 70
# D | 40 <= a < 55
# T | a < 40


class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    # Write your function here
    def calculate(self):
        sum = 0
        for score in scores:
            sum += score    
        average = sum/len(scores)
        if average < 40:
            return 'T'
        elif average < 55:
            return 'D'
        elif average < 70:
            return 'P'
        elif average < 80:
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return 'O'