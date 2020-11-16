#test cases starting from 0
class Solution:
    def fib(self, N):
      if N==0: return 0
      lastTwo = [1 , 1]
      counter = 3
      while counter <= N:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
      return lastTwo[1] if N > 1 else lastTwo[0]