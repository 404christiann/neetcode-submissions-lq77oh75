# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We need to run DFS recursively on each node.
        # Using DFS we are going to calculate the height of the leftmost & rightmost tree 

        # we need to create a result member variable to store the diameter calculation. 
        self.result = 0 

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            # this is our diameter
            self.result = max(self.result, left + right)
            # we dont return the diameter here, we want to return the max height.
            return max(left, right) + 1
        # we find the max heights for each subtree.
        dfs(root)
        # here we return the max diameter. 
        return self.result

        
