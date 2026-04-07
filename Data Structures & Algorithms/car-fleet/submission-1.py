class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            pair.append((p, s))
        stack = []
        pair.sort(reverse = True)
        for p, s in pair:
            dis = (target - p) / s
            stack.append(dis)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
