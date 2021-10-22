################################
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
################################

class Solution:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def sort_ascending(self):
        return sorted(self.dictionary.items(), key=lambda x: x[1])

    def sort_descending(self):
        return sorted(self.dictionary.items(), key=lambda x: x[1], reverse=True)

def main():
    dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    print(Solution(dictionary).sort_ascending())
    print(Solution(dictionary).sort_descending())

if __name__ == '__main__':
    main()

################################
# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
################################

# class Dictionary:
#     def __init__(self, d:dict):
#         self.d = d
    
#     def addKey(self):
#         print(self.d)
#         self.d[2] = 30         # Method 1
#         # self.d.update({2:30})# Method 2
#         print(self.d)
        
# def main():
#     givenDict = Dictionary({0: 10, 1: 20})
#     givenDict.addKey()

# if __name__ == '__main__':
#   main()

# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# class Dictionary(object):
#     def __init__(self, dic1: dict, dic2: dict, dic3: dict):
#         self.dic1 = dic1
#         self.dic2 = dic2
#         self.dic3 = dic3

#     def concatenate(self):
#         print(self.dic1)
#         print(self.dic2)
#         print(self.dic3)

#         # method 1
#         # self.dic1.update(self.dic2)
#         # self.dic1.update(self.dic3)
#         # return self.dic1

#         # method 2
#         return {**self.dic1, **self.dic2, **self.dic3}


# def main():
#     givenDict = Dictionary({1:10, 2:20}, {3:30, 4:40}, {5:50,6:60})
#     print(givenDict.concatenate())

# if __name__ == '__main__':
#     main()