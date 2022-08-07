"""
    PROMPT:
            Given an array of strings words and an integer k, return the k most frequent strings.

            Return the answer sorted by the frequency from highest to lowest.
            Sort the words with the same frequency by their lexicographical order.
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        word_count = dict()
        unique = []
        
        for item in words:
            if item in word_count:
                word_count[item] += 1
            else:
                word_count[item] = 1
                unique.append(item)
                
        if k > len(unique):
            k = len(unique)

        freq = self.merge_sort(unique, word_count)
        
        return freq[:k]
    
    
    def merge_sort(self, unique, count):
        if len(unique) <= 1:
            return unique
        
        mid = len(unique) // 2
        lefthalf = unique[:mid]
        righthalf = unique[mid:]
        
        left = self.merge_sort(lefthalf, count)
        right = self.merge_sort(righthalf, count)
        
        i, j, k = 0, 0, 0
        while (i < len(left)) and (j < len(right)):
            if count[left[i]] > count[right[j]]:
                unique[k] = left[i]
                i+=1
            elif count[left[i]] < count[right[j]]:
                unique[k] = right[j]
                j+=1
            elif count[left[i]] == count[right[j]]:
                if left[i] < right[j]:
                    unique[k] = left[i]
                    i+=1
                else:
                    unique[k] = right[j]
                    j+=1
            k+=1
                
        while (i < len(left)):
            unique[k] = left[i]
            i+=1
            k+=1
            
        while (j < len(right)):
            unique[k] = right[j]
            j+=1
            k+=1
            
        return unique
