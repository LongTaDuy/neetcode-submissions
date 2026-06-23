class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visited = {} # False: done visit, True: still in recursion
        res = []
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            visited[node] = False
            res.append(node)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)