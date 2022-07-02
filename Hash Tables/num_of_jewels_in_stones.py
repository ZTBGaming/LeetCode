"""
    PROMPT:
            You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
            Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

            Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
            J = length of jewels string
            S = length of stones string
            
            Time Complexity:    O(J+S)
            Space Complexity:   O(J)
        """
        # Initialize a counter variable
        counter = 0
        # Initialize a jewels set
        jewels_set = set()
        # loop through jewels
        for item in jewels:
            # Add to jewels set
            jewels_set.add(item)
        #loop through stones
        for rock in stones:
            # if stone in jewels, increment counter
            if rock in jewels_set:
                counter+=1
        # return counter
        return counter
