'''
Binary Tree Inorder Traversal

PROMPT: 
        Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''
# GIVEN BY LEETCODE
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

######## Iterative Solution ########
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:     
        
        
        
######## Recursive Solution ########
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        if root:
            preorder+=self.preorderTraversal(root.val)
            preorder+=self.preorderTraversal(root.right)
            preorder+=self.preorderTraversal(root.left)
        return preorder
'''
