# https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor

"""
You're given three inputs, all of which are instances of an AncestralTree class that have an ancenstor property pointing to their youngest ancestor. The first input is the top ancenstor in an ancestral tree(i.e  the only instance that has no ancestors --its propert points to None/null). and the other two inputs are descendants of the ancestral tree.

Write a function that returns the youngest common ancestor of the two descendants.

Note that a descendant is considered its own ancenstor. So in simple ancestral tree below, the youngest common ancestor to nodes A and B is node A.

// The youngest common ancestor to nodes A and B is node A.
     A
    /
   B

Sample Input:
// The nodes are from the ancestral tree shown above.
topAncestor = node A
descendantOne = node E
descendantTwo = node I
                A
            /       \   
           B          C 
        /   \       /  \
       D     E     F    G
      / \
     H   I

Sample Output:
node B
"""

# Explain the solution:
# Start by finding the two input descendants' depths in the ancestral tree. If one of them is deeper, iterate up through its ancestors until you reach the depth of the higher descendant.
# Then iterate up through both descendants' ancestors in tandem/parallel until you find the first common ancestor. 
# Note that at this point, one of the descendants will be the ancestor of the lower descendant that is at the same level as the higher descendant. 

class AncestralTree:
    def __init__(self, name): # name is the name of the node
        self.name = name # name of the node
        self.ancestor = None
   
# O(d) time | O(1) space, where d is the depth(height) of the ancenstral tree

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
      depthOne = getDescendantDepth(descendantOne, topAncestor)
      depthTwo = getDescendantDepth(descendantTwo, topAncestor)
      if depthOne > depthTwo: # if descendantOne is deeper
         return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo) # return the first common ancestor
      else:
         return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
      depth = 0
      while descendant != topAncestor: # while the descendant is not the top ancestor
         depth += 1 # increment the depth
         descendant = descendant.ancestor # move up the ancestral tree by one level
      return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff): # lowerDescendant is the lower descendant, higherDescendant is the higher descendant, and diff is the difference in depths
      while diff > 0:
         lowerDescendant = lowerDescendant.ancestor # move up the ancestral tree by one level
         diff -= 1 # decrement the difference
      while lowerDescendant != higherDescendant: # while the lower descendant is not the higher descendant
         lowerDescendant = lowerDescendant.ancestor # move up the ancestral tree by one level
         higherDescendant = higherDescendant.ancestor # move up the ancestral tree by one level
      return lowerDescendant # return the first common ancestor

