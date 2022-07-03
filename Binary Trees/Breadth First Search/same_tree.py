"""
    PROMPT:
            Given the roots of two binary trees p and q, write a function to check if they are the same or not.

            Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        left, right = False, False
        if (p and q):
            if (p.val != q.val):
                return False
            else:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
        elif (not p) and (not q):
            return True

        return (left and right)
