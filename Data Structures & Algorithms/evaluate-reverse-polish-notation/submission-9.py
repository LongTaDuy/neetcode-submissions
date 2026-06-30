class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(b - a)
                elif i == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
        return stack[0]
                