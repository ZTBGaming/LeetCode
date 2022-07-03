'''
Binary Tree PostOrder Traversal

PROMPT: 
        Given the root of a binary tree, return the postorder traversal of its nodes' values.
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:     
        postorder, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                postorder.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return postorder[::-1]
        
        
######## Recursive Solution ########
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        if root:
            postorder.append(root.val)
            postorder+=self.postorderTraversal(root.right)
            postorder+=self.postorderTraversal(root.left)
        return postorder
'''