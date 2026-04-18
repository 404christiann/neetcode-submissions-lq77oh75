# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # this problem is similar to the same tree problem. 
        # we will have a couple of base cases. 

        # Defining a sub tree: a tree that has the same node in "tree" and all of its node 
        # descendants (in other words, matching within a tree.)

        # traverse through the root and subroot, if node value is not the same 
        # lets move down the tree. Check the left and right side if they 
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    
    
    # use helper function isSameTree
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # three base cases: 
        # 1. when p and q are none, that means they are the same. 
        if not p and not q:
            return True
        # 2. if one is empy and the other isnt. 
        
        elif not p or not q or p.val != q.val:
            return False
        # 3. If the values arent the same. 
        # elif p.val != q.val:
        #     return False
        
        leftSubTree = self.isSameTree(p.left,q.left)
        rightSubTree = self.isSameTree(p.right,q.right)
        # this is the recursive step. 
        return leftSubTree and rightSubTree
    


            

             