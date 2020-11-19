# Singly linked list - Insert Node

# Note: If the head argument passed to the insert function is null, then the inital list is empty

# sample input
# 4
# 2
# 3
# 4
# 1

#sample output
# 2 3 4 1

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        print(data, end=' ')

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  