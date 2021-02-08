class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time - one loop | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList # headNode
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value: # when value of next node is equal to current node
			nextDistinctNode = nextDistinctNode.next # setting the pointer for nextDistinct Node
			
		currentNode.next = nextDistinctNode # removing duplicates
		currentNode = nextDistinctNode # changing the pointer to nextDistinct Node
	
	return linkedList