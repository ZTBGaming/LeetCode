"""
    PROMPT:
            
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = []
        
        length = len(s)
        start = length
        
        for i in range(length - 1, -1, -1):
            
            if s[i] == " ":
                text = s[i:start].strip()
                words.append(text[::-1])
                start = i + 1
        
        text = s[:start].strip()
        words.append(text[::-1])
                    
        return " ".join(words[::-1])
