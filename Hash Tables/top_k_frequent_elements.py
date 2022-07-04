"""
    PROMPT:
            Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize a counter hashmap
        counters = dict()
        freq_groups = dict()
        # Initialize a most frequent values
        freq = []
        # Track max freq count
        maxi = 0
        # Loop through nums
        for value in nums:
            #check if value is in hashmap
            if value in counters:
                # Increment count
                counters[value] += 1
            # Add value counter to hashmap
            else:
                counters[value] = 1
            
            if counters[value] in freq_groups:
                freq_groups[counters[value]].append(value)
            else:
                freq_groups[counters[value]] = [value]
                maxi = max(maxi, counters[value])

        for x in range(maxi, 0, -1):
            freq+=freq_groups[x]
            if len(set(freq)) >= k:
                return set(freq)
