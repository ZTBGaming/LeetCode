
'''
Path Sum of a Binary Tree

PROMPT: 
        Given the root of a binary tree and an integer targetSum, return true if the tree
        has a root-to-leaf path such that adding up all the values along the path equals targetSum.
        
        A leaf is a node with no children.
        
        Returns: is targetSum possible? (bool)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        
        # When no children exist, we know this is a leaf
        if not root.left and not root.right:
            return 0 == targetSum
       
        # Since there is more to this Tree, dive further while subtracting the node.val from targetSum
        else:
            left, right = False, False
            if root.left:
                left = self.hasPathSum(root.left, targetSum)
            if root.right:
                right = self.hasPathSum(root.right, targetSum)
            return left or right
