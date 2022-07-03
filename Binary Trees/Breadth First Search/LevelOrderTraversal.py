'''
Binary Tree Level Order Traversal

PROMPT: 
        Given the root of a binary tree, return the level order traversal of its nodes' values.
        (i.e., from left to right, level by level).
'''

# GIVEN BY LEETCODE
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

######## Iterative Solution ########
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # levelorder initializes empty since we may receive an empty tree
        # queue is an actual queue data structure imported from collections 
        levelorder, queue = [], deque([root])
        # Repeats indefinitely until stack is empty, then nextlevel is returned
        while True:
            
            stack, nextlevel = [], []
            while not (queue == deque([])):
                
                node = queue.popleft()
                if node:
                    stack.append(node.val)
                    nextlevel.append(node.left)
                    nextlevel.append(node.right)

            if stack == []:
                return levelorder
            else:
                levelorder.append(stack)
                queue = deque(nextlevel)