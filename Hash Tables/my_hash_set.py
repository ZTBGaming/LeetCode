"""
    PROMPT: Design a HashSet without using any built-in hash table libraries.
"""

class MyHashSet:

    def __init__(self):
        self.set = set()

    def add(self, key: int) -> None:
        """
            Inserts the value key into the HashSet.
        """
        self.set.add(key)

    def remove(self, key: int) -> None:
        """
            Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
        """
        if key in self.set:
            self.set.remove(key)

    def contains(self, key: int) -> bool:
        """
            Returns whether the value key exists in the HashSet or not.
        """
        return key in self.set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
