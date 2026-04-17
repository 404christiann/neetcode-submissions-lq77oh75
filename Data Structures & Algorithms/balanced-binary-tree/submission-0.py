# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # ok so, we will need to make a dfs helper method that will 
        # help us count the number of subtress of every node? 

        self.isBalanced = True

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            print(left,right)
            if abs(left - right) > 1: 
                self.isBalanced = False
            return 1 + max(left, right)
        dfs(root)
        return self.isBalanced


