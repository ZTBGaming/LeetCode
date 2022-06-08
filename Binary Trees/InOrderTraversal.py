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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return inorder
            node = stack.pop()
            inorder.append(node.val)
            root = node.right

        
######## Recursive Version ########
'''
        inorder = []
        if root:
            inorder+=self.inorderTraversal(root.left)
            inorder.append(root.val)
            inorder+=self.inorderTraversal(root.right)
        return inorder
'''