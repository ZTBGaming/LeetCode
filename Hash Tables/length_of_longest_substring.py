"""
    PROMPT:
            Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        BRUTE SLIDING WINDOW approach
        Time Complexity:    O(N^3) -> terrible
        Space Complexity:   O(N)
        """
        # Initialize two pointers
        i, j = 0, 0
        # Initalize substring len
        max_sub = 0
        # Initialize hashset
        hashset = set()
        # loop through pointers, leading with right side
        while (i < len(s)):
            while (j < len(s)):
                # If a new char isn't in hashset, add it
                if s[j] not in hashset:
                    hashset.add(s[j])
                # else set left pointer to right, increment right pointer
                else:
                    hashset = set()
                    j = i+1
                    break
                max_sub = max(max_sub, len(hashset))
                j+=1
            i+=1
        
        # return max length of unique strings
        return max_sub
