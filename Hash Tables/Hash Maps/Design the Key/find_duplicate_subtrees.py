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
        duplicates = set()
        tree_nodes = dict()
    
        def depth(root):
            routing = []
            if root:
                routing.append("~"+str(root.val)+"#")
                routing+=depth(root.left)
                routing+=depth(root.right)
                if routing:
                    string = "".join(routing)
            else:
                string = 'null'
            
            if string in tree_nodes:
                tree_nodes[string]+=1
                if tree_nodes[string] == 2 and root:
                    duplicates.add(root)
            else:
                tree_nodes[string] = 1
                
            return string
        
        depth(root)
        return duplicates
