class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0
        visited = set(deadends)
        if '0000' in visited:
            return -1
        q = deque(['0000'])
        res = 0
        while q:
            for _ in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return res
                if lock in visited:
                    continue
                visited.add(lock)
                for i in range(4):
                    for j in [-1, 1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        q.append(lock[:i] + digit + lock[i + 1:])
            res += 1
        return -1

                