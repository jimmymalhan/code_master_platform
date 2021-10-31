# A critical point in a linked list is defined as either a local maxima or a local minima.

# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

# Input: head = [3,1]
# Output: [-1,-1]
# Explanation: There are no critical points in [3,1].


from typing import List, Optional
# import ListNode
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idx = 0
        first_point = -1
        prev_point = -1
        min_dist, max_dist = math.inf, 0
        prev = None
        curr = head
        
        while curr:
            if prev and curr.next:
                if (prev.val < curr.val and curr.next.val < curr.val) or \
                (prev.val > curr.val and curr.next.val > curr.val):

                    if first_point == -1:
                        first_point = idx
                    max_dist = idx - first_point
                    if prev_point != -1:
                        min_dist = min(min_dist, idx - prev_point)
                    prev_point = idx
                    
            prev = curr
            curr = curr.next
            idx += 1
        
        if max_dist == 0:
            return [-1, -1]
        
        return [min_dist, max_dist]

def main():
    head = ListNode(3)
    head.next = ListNode(1)
    sol = Solution()
    print(sol.nodesBetweenCriticalPoints(head))

if __name__ == "__main__":
    main()