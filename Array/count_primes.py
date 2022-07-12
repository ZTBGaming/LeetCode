"""
    PROMPT:
            Given an integer n, return the number of prime numbers that are strictly less than n.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        # 0 and 1 are not prime numbers, therefore to get an output we need to start above n=2
        if n <= 2:
            return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = 0
                
        return sum(primes)
