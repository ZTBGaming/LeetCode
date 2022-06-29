"""
    PROMPT:
            Given two integer arrays nums1 and nums2: 
            
            Return an array of their intersection.
            Each element in the result must be unique and you may return the result in any order.
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        test_set, answer = set(), set()
        for i in nums1:
            test_set.add(i)
            
        for j in nums2:
            if j in test_set:
                answer.add(j)
        
        return answer
