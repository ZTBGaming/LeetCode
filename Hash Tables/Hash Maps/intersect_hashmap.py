"""
    PROMPT:
            Given two integer arrays nums1 and nums2, return an array of their intersection.
            Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_nums = dict()
        answer = []
        
        for item in nums1:
            if item in first_nums:
                first_nums[item] += 1
            else:
                first_nums[item] = 1
                
        for item in nums2:
            if item in first_nums and first_nums[item] > 0:
                answer.append(item)
                first_nums[item] -= 1
                
        return answer
