class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxcnt = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        valCnt = self.cnt.get(val, 0) + 1
        self.cnt[val] = valCnt
        if self.maxcnt < valCnt:
            self.maxcnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)


    def pop(self) -> int:
        res = self.stacks[self.maxcnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxcnt]:
            self.maxcnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()