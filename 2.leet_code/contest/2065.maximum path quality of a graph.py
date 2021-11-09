# https://leetcode.com/problems/maximum-path-quality-of-a-graph/
# 2065. Maximum Path Quality of a Graph

# There is an undirected graph with n nodes numbered from 0 to n - 1 (inclusive). You are given a 0-indexed integer array values where values[i] is the value of the ith node. You are also given a 0-indexed 2D integer array edges, where each edges[j] = [uj, vj, timej] indicates that there is an undirected edge between the nodes uj and vj, and it takes timej seconds to travel between the two nodes. Finally, you are given an integer maxTime.

# A valid path in the graph is any path that starts at node 0, ends at node 0, and takes at most maxTime seconds to complete. You may visit the same node multiple times. The quality of a valid path is the sum of the values of the unique nodes visited in the path (each node's value is added at most once to the sum).

# Return the maximum quality of a valid path.

# Note: There are at most four edges connected to each node.

# Input: values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
# Output: 75
# Explanation of the solution:
# The path 0 -> 1 -> 2 is valid since the total time is 10 + 15 = 25 and the quality is (0 + 32) + (1 + 10) + (2 + 43) = 75.

from typing import List
import collections
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        ans = 0 # ans is the max quality of a valid path
        graph = collections.defaultdict(dict) # graph is a dict of dicts # {0: {1: 10, 3: 10}, 1: {0: 10, 2: 15}, 2: {1: 15}, 3: {0: 10}}
        for u, v, t in edges: # u is the parent node, v is the child node, t is the time
            graph[u][v] = t # graph[u][v] is the time from u to v
            graph[v][u] = t # graph[v][u] is the time from v to u
        
        def dfs(curr, visited, score, cost): # curr is the current node, visited is the list of visited nodes, score is the sum of the values of the visited nodes, cost is the time cost of the path
            if curr == 0: # if curr is the root node
                nonlocal ans # nonlocal is used to modify the global variable
                ans = max(ans, score) # update the max quality of a valid path
            
            for nxt, time in graph[curr].items(): # nxt is the child node, time is the time from curr to nxt
                if time <= cost: # if the time from curr to nxt is less than or equal to the time cost of the path
                    dfs(nxt, visited|set([nxt]), score+values[nxt]*(nxt not in visited), cost-time) # dfs the child node
        
        dfs(0, set([0]), values[0], maxTime) # dfs the root node
        return ans

def main():
    a = Solution()
    print(a.maximalPathQuality([0,32,10,43], [[0,1,10],[1,2,15],[0,3,10]], 49))

if __name__ == "__main__":
    main()