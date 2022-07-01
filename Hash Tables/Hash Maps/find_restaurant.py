"""
    PROMPT:
            Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

            You need to help them find out their common interest with the least list index sum. 
            If there is a choice tie between answers, output all of them with no order requirement.
            You could assume there always exists an answer.
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = dict()
        duplicates = dict()
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in hashmap:
                duplicates[list2[j]] = hashmap[list2[j]]+j

        minimum = 5000
        restaurants = []
        for key, value in duplicates.items():
            if value < minimum:
                restaurants = [key]
                minimum = value
            elif value == minimum:
                restaurants.append(key)
        
        return restaurants
