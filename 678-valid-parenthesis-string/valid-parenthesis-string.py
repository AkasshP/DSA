class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        _star = []
        for i, ch in enumerate(s):
            if ch == ')' or ch == '*':
                if ch == ')':
                    if stack and s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        if _star:
                            _star.pop()
                        else:
                            return False
                if ch == '*':
                    _star.append(i)
            else:
                stack.append(i)
        #final validation
        while stack and _star:
            if stack[-1] < _star[-1]:
                stack.pop()
                _star.pop()
            else:
                break

        return not stack

