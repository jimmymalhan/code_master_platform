# If Argument for intialAge is negative > constructor should set to 0
# Year passed() age increased by 1
# For amIold():
# if age < 13, print you are young.
# if age >= 13 and age < 18 print You are a teenager
# Otherwise, print You are old 

#Constraints
# 1 =< T <= 4
# -5 <= age <= 30

class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            self.initialAge = 0
        else :
            self.initialAge = initialAge

    def amIOld(self):
        if self.initialAge < 13:
            print('You are young.')
        elif self.initialAge < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        self.initialAge += 1
