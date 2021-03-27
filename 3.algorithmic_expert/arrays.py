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

# # for i in range(len(array)):
# #     print(array[i]) # 1, 2, 3, 4
# #     # print(i) # 0, 1, 2, 3, 4

# def range1(start, end):
#     return range(start, end+1)
# print(range1(1,10))

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

chara = "abccc"
doc = "abcccc"
def Solution(doc, chara):
    for element in chara:
        if doc.count(element) > chara.count(element):
            return False
    return True


print(Solution(doc,chara))