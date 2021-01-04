array = [1, 2, 3, 4]

# print(array) # [1, 2, 3, 4]
# for i in range(len(array) - 1):
# # for i in range(len(array)): # index out out bound
#     print(array[i]+array[i+1], end=' ') #3, 5, 7

# for i in range(len(array)):
#     print(array[i]) # 1, 2, 3, 4
#     # print(i) # 0, 1, 2, 3, 4

#  = equal
#  == equalized

def range1(start, end):
    return range(start, end+1)
print(range1(1,10))