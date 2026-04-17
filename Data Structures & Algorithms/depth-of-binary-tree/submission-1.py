# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # we need to use depth first search (recursively)
        if root is None: 
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        # we get the max depth between the left and right sides. 
        # we use plus one since we need to account 
        return max(leftDepth, rightDepth) + 1
    