class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Phone keypad mapping
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []
        result = []
        def backtrack(index,strr):

            if index == len(digits):
                result.append(strr)
                return
            
            letters = phone_map[digits[index]]

            for l in letters:
                backtrack(index + 1,strr + l)
            
        backtrack(0,"")
        return result
        
        