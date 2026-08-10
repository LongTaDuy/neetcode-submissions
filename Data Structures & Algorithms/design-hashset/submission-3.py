class MyHashSet:

    def __init__(self):
        self.build = [False] * 1000001

    def add(self, key: int) -> None:
        self.build[key] = True

    def remove(self, key: int) -> None:
        self.build[key] = False
                
    def contains(self, key: int) -> bool:
        if self.build[key] == True:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)