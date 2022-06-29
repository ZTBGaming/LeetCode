"""
    PROMPT: Given an integer array nums: 
    
            Return true if any value appears at least twice in the array,
            Return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        test_set = set()
        
        for i in nums:
            if i in test_set:
                return True
            test_set.add(i)
        
        return False

"""
~ very simple solution ~
~ (don't think this is what they want you to do) ~

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
"""
