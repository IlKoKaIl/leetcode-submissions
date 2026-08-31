# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            left_ok = dfs(node.left, low, node.val)

            right_ok = dfs(node.right, node.val, high)

            return left_ok and right_ok

        return dfs(root, float('-inf'), float('inf'))
                

            
                
        