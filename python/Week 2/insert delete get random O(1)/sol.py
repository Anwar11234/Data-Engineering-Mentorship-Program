import random 

class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.vals = []
        self.index = 0

    def insert(self, val: int) -> bool:
        res = val not in self.set
        if res:
            self.vals.append(val)
            self.set[val] = self.index
            self.index += 1
        return res

    def remove(self, val: int) -> bool:
        res = val in self.set
        if res:
            removed_value_index = self.set[val]
            lastVal = self.vals[-1]
            self.vals[removed_value_index] = lastVal
            self.vals.pop()
            self.index -= 1
            self.set[lastVal] = removed_value_index
            del self.set[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()