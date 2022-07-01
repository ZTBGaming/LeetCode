"""
    PROMPT:
            Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = dict()
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]] = 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
