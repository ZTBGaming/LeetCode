"""
    PROMPT:
            Implement the RandomizedSet class:

            RandomizedSet()         Initializes the RandomizedSet object.
            
            bool insert(int val)    Inserts an item val into the set if not present.
                                    Returns true if the item was not present, false otherwise.
                                    
            bool remove(int val)    Removes an item val from the set if present.
                                    Returns true if the item was present, false otherwise.
                                    
            int getRandom()         Returns a random element from the current set of elements
                                    (it's guaranteed that at least one element exists when this method is called).
                                    Each element must have the same probability of being returned.
                                    
            You must implement the functions of the class such that each function works in average O(1) time complexity.
"""

import random

class RandomizedSet:

    def __init__(self):
        self.values = dict()
        self.value_index = dict()
        self.length = 0
        
    def insert(self, val: int) -> bool:
        if val in self.values:
            return False

        self.values[val] = self.length
        self.value_index[self.length] = val
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False

        old_index = self.values.pop(val)
        if old_index < self.length - 1:
            reset_value = self.value_index.pop(self.length - 1)
            self.value_index[old_index] = reset_value
            self.values[reset_value] = old_index
        else:
            self.value_index.pop(self.length-1)
        self.length -= 1
        return True

    def getRandom(self) -> int:
        print(self.length)
        rando = random.randrange(0, self.length)
        return self.value_index[rando]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
