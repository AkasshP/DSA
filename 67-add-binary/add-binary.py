class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #approach convert the bits from binary to number then convert to original form
        num1 = int(a,2)
        num2 = int(b,2)
        result = bin(num1 + num2)
        return str(result[2:])