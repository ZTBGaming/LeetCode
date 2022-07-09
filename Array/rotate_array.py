"""
    PROMPT:
            Given an array, rotate the array to the right by k steps, where k is non-negative.
            
            Time Complexity:    O(N)
            Space Complexity:   O(N)
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1 or k%len(nums)==0:
            return
        visited = set()
        length = len(nums)
        i, j = 0, 0
        
        while j not in visited:
            i = j
            pointer = nums[i]
            while i % length not in visited:
                visited.add(i%length)
                pointer, nums[(i+k) % length] = nums[(i+k) % length], pointer
                i+=k
            j+=1
            
"""
NOTE: Simpler solution, but O(2*N) and O(N) Time/Space complexities

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new = dict()
        
        for i in range(len(nums)):
            new[(i+k)%len(nums)] = nums[i]
            
        for i in range(len(nums)):
            nums[i] = new[i]
                    
        return nums
"""
