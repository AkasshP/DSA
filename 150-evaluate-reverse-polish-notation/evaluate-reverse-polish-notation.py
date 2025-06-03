class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in {"+", "-", "*", "/"}:
                # Pop b, a
                b = stack.pop()
                a = stack.pop()

                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:  
                    stack.append(int(a / b))
            else:
                stack.append(int(tok))

        return stack[0]
                