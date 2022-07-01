"""
    PROMPT:
            Given an array of strings strs, group the anagrams together. You can return the answer in any order.

            An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            sorted_string = self.merge_sort(word)
            if sorted_string in anagrams:
                anagrams[sorted_string].append(word)
            else:
                anagrams[sorted_string] = [word]
        
        values_grouping = []
        for key, value in anagrams.items():
            values_grouping.append(value)
        
        return values_grouping
    
    def merge_sort(self, word):
        if len(word) <= 1:
            return word

        mid = len(word)//2
        lefthalf = word[:mid]
        righthalf = word[mid:]

        sorted_left = self.merge_sort(lefthalf)
        sorted_right = self.merge_sort(righthalf)

        i,j = 0,0
        sorted_string = []
        while (i < len(sorted_left)) and (j < len(sorted_right)):
            if sorted_left[i] < sorted_right[j]:
                sorted_string.append(sorted_left[i])
                i+=1
            else:
                sorted_string.append(sorted_right[j])
                j+=1

        while (i < len(sorted_left)):
            sorted_string.append(sorted_left[i])
            i+=1

        while (j < len(sorted_right)):
            sorted_string.append(sorted_right[j])
            j+=1

        return "".join(sorted_string)
    
"""
This is about 4x faster than above algorithm, however, does not 'personally' sort the strings. Uses more efficient, built-in python tool -> sorted()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for word in strs:
            sorted_string = "".join(sorted(word))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(word)
            else:
                anagrams[sorted_string] = [word]
        
        values_grouping = []
        for key, value in anagrams.items():
            values_grouping.append(value)
        
        return values_grouping
""""
