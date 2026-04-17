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

        return max(leftDepth, rightDepth) + 1
    

    # # Recursive DFS function
    # def dfs_recursive(tree, node, visited=None):
    #     if visited is None:
    #         visited = set()  # Initialize the visited set
    #     visited.add(node)    # Mark the node as visited
    #     print(node)          # Print the current node (for illustration)
    #     for child in tree[node]:  # Recursively visit children
    #         if child not in visited:
    #             dfs_recursive(tree, child, visited)

    # # Run DFS starting from node 'A'
    # dfs_recursive(tree, 'A')