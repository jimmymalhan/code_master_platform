# Singly linked list
# Complete the insert function -> increases the new Node
# (pass data as the Node constructor argument)
# and insert it to the tail of the linked list reference by the head parameter.
# Once the new node is added, return the reference to the head node

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
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head)	  