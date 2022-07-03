"""
    PROMPT:
            Given the root of a binary tree, return all duplicate subtrees.

            For each kind of duplicate subtrees, you only need to return the root node of any one of them.
            Two trees are duplicate if they have the same structure with the same node values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashmap = dict()
        duplicates = []
        
        def preorder(root):
            if root:
                path = str(root.val)
                path += "(" + preorder(root.left) + ")"
                path += "(" + preorder(root.right) + ")"
            else:
                path = "NULL"
            
            if (path in hashmap) and (path != "NULL"):
                if (hashmap[path] == 1):
                    duplicates.append(root)
                    hashmap[path] += 1
            elif (path != "NULL"):
                hashmap[path] = 1
                
            return path
            
        preorder(root)
        return duplicates 
