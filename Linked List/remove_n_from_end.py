"""
    PROMPT:
            Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        position, head = self.depth_search(head, n)
        return head
    
    def depth_search(self, node, n):
        if node:
            position, node.next = self.depth_search(node.next, n)
            if position == n:
                return position+1, node.next
            else:
                return position+1, node
        else:
            return 1, None
