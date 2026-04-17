# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # It is the same if the left and right nodes are the same between
        # p and q
        
        # brute force approach: 
        # recursively check if both trees node values are the same.
        # if the p.value == q.value then the trees are the same.

        # three base cases: 
        # 1. when p and q are none, that means they are the same. 
        if p is None and q is None:
            return True
        # if one is empy and the other isnt. 
        if p is None and q:
            return False
        if p and q is None:
            return False
        if p.val != q.val:
            return False
        
        leftNode = self.isSameTree(p.left,q.left)
        rightNode = self.isSameTree(p.right,q.right)
        
        return leftNode and rightNode
        
