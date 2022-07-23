"""
    PROMPT:
            Given a signed 32-bit integer x, return x with its digits reversed.
            
            If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            neg = -1
        else:
            neg = 1
        
        new_num = str(abs(x))
        new_num = new_num[::-1]
        for i in range(len(new_num)):
            if new_num[i] != '0':
                break
        
        new_num = new_num[i:]
        new_num = int(new_num) * neg
        
        if new_num < (-2 ** 31) or new_num > ((2 ** 31) - 1):
            return 0
        else:
            return new_num
