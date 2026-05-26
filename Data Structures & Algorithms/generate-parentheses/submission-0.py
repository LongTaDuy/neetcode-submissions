class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(temp))
                return 
            if openN < n:
                temp.append("(")
                backtrack(openN + 1, closeN)
                temp.pop()
            
            if closeN < openN:
                temp.append(")")
                backtrack(openN, closeN + 1)
                temp.pop()
        backtrack(0, 0)
        return res