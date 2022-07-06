"""
    PROMPT:
            The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence.
            Each number is the sum of the two preceding ones, starting from 0 and 1. That is,

            F(0) = 0, F(1) = 1
            F(n) = F(n - 1) + F(n - 2), for n > 1
            
            Given n, calculate F(n).
"""

storage = {0: 0, 1: 1}

class Solution:
    def fib(self, n: int) -> int:
        if n in storage:
            return storage[n]
        else:
            storage[n] = self.fib(n-1) + self.fib(n-2)
        return storage[n]
