# for v in zip(*array) -> ([1,2],[3,4]) or slice [1:-1]
# split and then loop through a string -> to modify string
# declare a variable -> arrIdx = 0 and loop through to check arrIdx < len(array) or arrIdx == len(array)
# nested loops -> for i in .. for j in i - Ques1

# array = [1, 2, 3, 4]
# for i in range(len(array) - 2):
#     print(i)
# for i in range(len(array) - 1):
# for i in range(len(array)): # index out out bound
    # print(array[i + 1]) # 2, 3, 4
    # print(array[i]+array[i+1], end=' ') #3, 5, 7


#Ques 1- 
# array = ([1,2],[3,4])
# # output = 1, 3, 2, 4
# newList = []
# for v in zip(*array):
#     # (1, 3)
#     # (2, 4)
#     for n in v:
#         # print(n)
#         # 1
#         # 3
#         # 2
#         # 4
#         newList.append(n)
# print(newList)
# # print(', '.join([str(n) for v in zip(*array) for n in v]))


# x = ["apple", "banana", "cherry"]
# for idx,value in enumerate(x):
#     print(idx, value)
# 0 apple
# 1 banana
# 2 cherry

# x = ["apple", "banana", "cherry"]
# for idx,value in enumerate(x, start=1):
#     print(idx, value)
# 1 apple
# 2 banana
# 3 cherry

#anagram
# a = "abc"
# b = "acb"
# def Solution(a, b):
#     if sorted(a) == sorted(b):
#         return True
#     else:
#         return False

# print(Solution(a,b))
# or 
# doc = "acccb"
# chara = "abccc"
# def Solution(doc, chara):
#     for element in chara:
#         if doc.count(element) > chara.count(element):
#             return False
#     return True


# print(Solution(doc,chara))

# string = "abcdcaf" - 7 elements
# for i in range(len(string)): # idx[0-6]
#     # for j in range(len(string)): # idx[0-6] - 7 times
#     for j in range(i, len(string)): # idx[0-6], [1-6], [2-6], [3-6], [4-6], [5,6],[6]

# count from list
# https://stackoverflow.com/questions/20510768/count-frequency-of-words-in-a-list-and-sort-by-frequency
# from collections import Counter
words =["hello world","b","b"]

def Solution(words = None):
    # return dict((i, words.count(i)) for i in words) #{'hello world': 1, 'b': 2}
    # for i in words:
    #     print(dict(i, words.count(i)))

#     # return Counter(words) # Counter({'b': 2, 'hello world': 1})
#     dic = {}
#     for i in words:
#         dic[i] = dic.get(i, 0) + 1
#         return dic # {'hello world': 1}


if __name__ == '__main__':
    print(Solution(words))
