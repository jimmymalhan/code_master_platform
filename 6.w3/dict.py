################################
# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
################################

# class Solution:
#     def __init__(self, dictionary):
#         self.dictionary = dictionary

#     def sort_ascending(self):
#         return sorted(self.dictionary.items(), key=lambda x: x[1])

#     def sort_descending(self):
#         return sorted(self.dictionary.items(), key=lambda x: x[1], reverse=True)

# def main():
#     dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#     print(Solution(dictionary).sort_ascending())
#     print(Solution(dictionary).sort_descending())

# if __name__ == '__main__':
#     main()

################################
# 2. Write a Python script to add a key to a dictionary. Go to the editor

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
################################

# class Dictionary:
#     def __init__(self, d:dict):
#         self.d = d
    
#     def addKey(self):
#         print(f'original_key:', self.d)
#         # method 1
#         # self.d[2] = 30

#         # method 2
#         # self.d.update({2:30})
#         # print(f'updated_key:', self.d)
#         # method 3
#         self.d = {**self.d, 2:30}
#         print(f'updated_key:', self.d)
        
# def main():
#     givenDict = Dictionary({0: 10, 1: 20})
#     givenDict.addKey()

# if __name__ == '__main__':
#   main()

################################
# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
################################

# class Dictionary(object):
#     def __init__(self, dic1: dict, dic2: dict, dic3: dict) -> None:
#         self.dic1 = dic1
#         self.dic2 = dic2
#         self.dic3 = dic3

#     def concatenate(self):
#         # print(self.dic1)
#         # print(self.dic2)
#         # print(self.dic3)

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

################################
# 4. Write a Python script to check whether a given key already exists in a dictionary
################################

# class Solution:
#     def __init__(self, dictionary:dict()) -> None:
#         self.dictionary = dictionary
    
#     def check_key(self, key:int) -> bool:
#         return key in self.dictionary

# def main():
#     givenDict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#     givenSolution = Solution(givenDict)
#     print(givenSolution.check_key(5))

# if __name__ == '__main__':
#     main()