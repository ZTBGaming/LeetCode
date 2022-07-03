'''
Maximum Depth of Binary Tree

PROMPT: 
        Given the root of a binary tree, return the maximum depth.
        
        Returns: number of levels (int)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        left, right = 0, 0
        if root:
            left = 1 + self.maxDepth(root.left)
            right = 1 + self.maxDepth(root.right)
            if left > right:
                return left
            else:
                return right
        else:
            return 0
