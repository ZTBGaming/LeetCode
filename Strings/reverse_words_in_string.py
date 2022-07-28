"""
    PROMPT:
            Given an input string s, reverse the order of the words.

            A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

            Return a string of the words in reverse order concatenated by a single space.

            Note that s may contain leading or trailing spaces or multiple spaces between two words.
            The returned string should only have a single space separating the words. Do not include any extra spaces.
            
            Time Complexity:    O(N)
            Space Complexity:   O(N)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        start = 0
        words = []
        
        s = s.strip()
        length = len(s)
        
        for i in range(length):
            
            if s[i] == " ":
                if (i+1 < length) and (s[i+1] != " "):
                    words.append(s[start:i].strip())
                    start = i
                    
        words.append(s[start:length].strip())
                    
        return " ".join(words[::-1])
