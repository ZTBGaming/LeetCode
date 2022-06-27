'''
Symmetric Tree

PROMPT: 
        Given the root of a binary tree, check whether it is a mirror of itself
        (i.e., symmetric around its center).
        EXAMPLE TREE:
            Input: root = [1,2,2,3,4,4,3]
            Output: true
                        1
                    2   |   2
                  3   4 | 4   3
                        |
        center line ->  |
        
        Returns: is it symmetric? (bool)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left, right = [], []
        left_traversal, right_traversal = [root.left], [root.right]
    
        # When this exits, left_traversal will be an array containing the reversed postorder traversal of the left side of the tree
        while left_traversal:
            node = left_traversal.pop()
            if node:
                left.append(node.val)
                left_traversal.append(node.left)
                left_traversal.append(node.right)
            else:
                left.append(None)
                
        # When this exits, right_traversal will be an array containing the preorder traversal of the left side of the tree
        while right_traversal:
            node = right_traversal.pop()
            if node:
                right.append(node.val)
                right_traversal.append(node.right)
                right_traversal.append(node.left)
            else:
                right.append(None)
                
        return left == right
