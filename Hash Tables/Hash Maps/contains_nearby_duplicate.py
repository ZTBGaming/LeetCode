"""
    PROMPT:
            Given an integer array nums and an integer k, 
            Return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] in hashmap and abs(i - hashmap[nums[i]]) <= k:
                return True
            hashmap[nums[i]] = i
        return False
