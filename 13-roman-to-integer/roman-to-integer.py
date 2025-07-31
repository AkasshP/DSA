class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        n = len(s)
        if n > 1:
            for i in range(n-1,-1,-1):
                if i - 1 > -1: 
                    if  roman[s[i]] > roman[s[i-1]]:
                        if not result:
                                result = roman[s[i]] - roman[s[i-1]]
                        else:
                                result -= roman[s[i-1]]
                    else:
                        if not result:
                            result = roman[s[i-1]] + roman[s[i]]
                        else:
                            result += roman[s[i-1]]
            return result
        else:
            return roman[s[0]]
