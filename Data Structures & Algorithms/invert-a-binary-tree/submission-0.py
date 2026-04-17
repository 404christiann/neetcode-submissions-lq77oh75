# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # The concept here is at each node check if you have a right & left node.
        # if you have either, we are going to want to switch them. 
        # so your original left will now be your right..vice versa. 

        # you continue to do this till you have no left or rights (until they point to None.)

        # The overall concept here is changing the pointers. (left and right to be exact)

        # Structuring the while loop: while we still have a left and right node we traverse. 
        
        #base case: if the root is None, return none
        if not root:
            return None

        # tuple unpacking - temporarily save the variables first.
        root.left, root.right = root.right, root.left
        # we need to figure out how to backtrack in this tree? 
        # Answer: Using recursion. 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

