# Task:
# class constructor to takes integer as parameter and saves it to the elements instance variable
# compute difference method that finds the maximum absolute difference between any 2 numbers in N and stores it i maximumDifference instance variable

# constraints
# 1 <= N <= 10
# 1 <= elements[i] <= 100 where 0 <= i<= N-1

class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
        self.maximumDifference = 0

    def computeDifference(self):
        min_element = 101
        max_element = 0

        for element in self.__elements:
            if element < min_element:
                min_element = element
            elif element > max_element:
                max_element = element

        self.maximumDifference = abs(min_element - max_element)
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)