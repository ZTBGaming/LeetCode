"""
    PROMPT:
            Given two strings s and t, return true if t is an anagram of s, and false otherwise.

            An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
            typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = dict()
                
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
                
        for char in t:
            if char in hashmap and hashmap[char] == 0:
                return False
            if char not in hashmap:
                return False
            else:
                hashmap[char] -= 1
        
        return True
