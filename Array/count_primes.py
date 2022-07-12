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
        # Initializing int's 0 and 1 as non-primes
        primes[0] = primes[1] = 0
        
        # Any number that is not prime will be divisible by a number less than, 
        # or equal to it's square root and the paired number greater than,
        # or equal to it's square root
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                # If a number is prime then we know all multiples of it are NOT prime
                for j in range(i*i, n, i):
                    primes[j] = 0
                
        return sum(primes)
