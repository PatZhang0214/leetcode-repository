from typing import Dict, Set
import random

class RandomizedSet:
    randomSet = dict()
    length = 0
    values = set()
    def __init__(self):
        self.randomSet = {}
        self.length = 0
        self.values = set()

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.randomSet[val] = val
        self.values.add(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        self.randomSet.pop(val)
        self.values.pop(val)
        self.length -= 1
        return True

    def getRandom(self) -> int:
        randomIndex = random.randint(0, self.length - 1)
        return self.randomSet.values[randomIndex]

if __name__ == '__main__':
    s = RandomizedSet()
    print(s.insert(1))
    print(s.remove(2))
    print(s.insert(2))
    print(s.getRandom())
    print(s.remove(1))
    print(s.insert(2))
    print(s.getRandom())






