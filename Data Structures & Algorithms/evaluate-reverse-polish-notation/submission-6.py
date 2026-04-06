class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = ['+', '-', '*', '/']
        if len(tokens) == 0:
            return 0
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in lst:
                stack.append(tokens[i])
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    result = int(a) + int(b)
                    stack.append(result)
                elif tokens[i] == '-':
                    result = int(a) - int(b)
                    stack.append(result)
                elif tokens[i] == '*':
                    result = int(a) * int(b)
                    stack.append(result)
                elif tokens[i] == '/':
                    result = int(int(a) / int(b))
                    stack.append(result)

        return stack[0]
        