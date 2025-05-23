class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = list(str(int(''.join(str(n) for n in digits)) + 1))
        result = [int(n) for n in b]
        return result

        
        