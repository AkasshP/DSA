class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # new_token = tokens.copy()
        # if len(tokens) == 1:
        #     return int(tokens[0])
        # result = ''
        # def newtrunc(val1,val2):
        #     return str(int(int(val1) / int(val2)))
        # def trunc(res,val):
        #     print(res,'checking-trunc')
        #     return str(int(int(val) / eval(res)))
        # def reversepolish(new_token,result):
        #     if new_token:
        #         for i in range(len(new_token)):
        #             if new_token[i] == '+' or new_token[i] == '-' or new_token[i] == '*' or new_token[i] == '/':
        #                 if result == '':
        #                     if new_token[i] == '/':
        #                         val = newtrunc(new_token[i-2],new_token[i-1])
        #                         result = '('+ val +')'
        #                         new_token.pop(i)
        #                         new_token.pop(i-1)
        #                         new_token.pop(i-2)
        #                         return reversepolish(new_token,result)
        #                     else:
        #                         result = '('+ new_token[i-2] + new_token[i] + new_token[i-1] +')'
        #                         new_token.pop(i)
        #                         new_token.pop(i-1)
        #                         new_token.pop(i-2)
        #                         print(result,'checking',i)
        #                         return reversepolish(new_token,result)
        #                 else:
        #                     if new_token[i] == '/':
        #                         val = trunc(result,new_token[i-1])
        #                         result = '('+ val +')'
        #                         new_token.pop(i)
        #                         new_token.pop(i-1)
        #                         return reversepolish(new_token,result)
        #                     else:
        #                         result = '('+ new_token[i-1] + new_token[i] + result +')'
        #                         new_token.pop(i)
        #                         new_token.pop(i-1)
        #                         return reversepolish(new_token,result)
        #     else:
        #         return result

        # res = reversepolish(new_token,result)
        # return eval(res)
        stack: List[int] = []

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
                