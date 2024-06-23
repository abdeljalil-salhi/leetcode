import random


class RandomizedSet:

    def __init__(self):
        self.val = []

    def insert(self, val: int) -> bool:
        if val in self.val:
            return False
        self.val.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.val:
            self.val.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.val)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
