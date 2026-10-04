class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}
        indegree = {c : 0 for c in adj}
        for w in range(len(words) - 1):
            w1, w2 = words[w], words[w + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > min_len and w1[:min_len] == w2[:min_len]:
                return ""
            for i in range(min_len):
                if w1[i] != w2[i]:
                    if w2[i] not in adj[w1[i]]:
                        adj[w1[i]].add(w2[i])
                        indegree[w2[i]] += 1
                    break
        q = deque()
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for i in adj[char]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if len(res) != len(indegree):
            return ""
        return "".join(res)

            
            
