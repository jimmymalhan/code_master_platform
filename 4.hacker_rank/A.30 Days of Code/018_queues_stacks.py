# s is palindrome? reads backwords and forwards
# for each character in s, enqueue it in a queue
# also pushes same character in a stack
# dequeue the first character from the queue and
# pop the top character off the stack, then
# compare the two characters to see if they are
# the same ; 
# as long as the character match- > continue
# until containers are empty (palindrome)

# stack and queues are list data structure
# Queues = FIFO //list
# Stack = FILO //list

class Solution:
# Write your code here
    def __init__(self):
        self.stack = list()
        self.queue = list()

    def pushCharacter(self, char):
        self.stack.append(char)

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        return (self.stack.pop(-1))

    def dequeueCharacter(self):
        return (self.queue.pop(0))
        
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    