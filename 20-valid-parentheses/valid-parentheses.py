class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        if len(s) < 2:
            return False
        else:
            for st in s:
                if st in pairs.values():
                    stack.append(st)
                elif st in pairs.keys():
                    if len(stack) > 0:
                        if pairs[st] == stack[-1]:
                            stack.pop()
                        else:
                            return False
                    else:
                        return False

            if len(stack) > 0:
                return False
            else:
                return True
        #reversing logic
        # for i in pairs.values:
        #     if  i == '(' or i == '{' or i == '[':
        #         arr.append(i)

        #     else:
        #         print('string',i)
        #         arr.reverse()
        #         print(arr,'arr-reverse')
        #         if arr[-1] == i:
        #             arr.pop()
        #         else:
        #             return False
        #     print(arr,'check')
        return True
