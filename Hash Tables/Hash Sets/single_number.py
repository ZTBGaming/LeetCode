"""
    PROMPT:
            Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

            You must implement a solution with a linear runtime complexity and use only constant extra space.
            
            Time Complexity: O(N)
            Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        test_set = set()
        for x in nums:
            if x in test_set:
                test_set.remove(x)
            else:
                test_set.add(x)
        return test_set.pop()
