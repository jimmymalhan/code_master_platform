# https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor

"""
You're given three inputs, all of which are instances of an AncestralTree class that have an ancenstor property pointing to their youngest ancestor. The first input is the top ancenstor in an ancestral tree(i.e  the only instance that has no ancestors --its propert points to None/null). and the other two inputs are descendants of the ancestral tree.

Write a function that returns the youngest common ancestor of the two descendants.

Note that a descendant is considered its own ancenstor. So in simple ancestral tree below, the youngest common ancestor to ndes A and B is node A.

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
# Start by finding the two input descendants' depths in the ancesntral tree. If one of them is deeper, iterate up through its ancestors until you reach the depth of the higher descendant.
# Then iterate up through both descendants' ancestors in tandem until you find the first common ancestor. 
# Note that at this point, one of the descendants will be the ancestor of the lower descendant that is at the same level as the higher descendant. 

# O(d) time | O(1) space, where d is the depth(height) of the ancenstral tree