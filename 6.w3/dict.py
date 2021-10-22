# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

class Solution():
    def __init__(self, d: dict):
        self.d = d

    def toQuestion(self):
        s = dict(sorted(self.d.items(), key=lambda x: x[1])) # sorted
        k = dict(sorted(self.d.items(), key=lambda x: x[1], reverse = True)) # sorted reversed
        print(s)
        print(k)

def main():
    givenDict = Solution({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
    givenDict.toQuestion()

if __name__ == '__main__':
  main()