# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

# class Solution():
#     def toQuestion():
#       pass

# def main():
#   givenString1 = Solution({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
#   givenString1.toQuestion()


# if __name__ == '__main__':
#   main()


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
s = dict(sorted(d.items(), key=lambda x: x[1])) # sorted
k = dict(sorted(d.items(),key=lambda x:x[1],reverse = True)) # sorted reversed

print(d)
print(s)
print(k)

# to do - tu put this into class