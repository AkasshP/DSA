class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        temp = []
        final_result = []
        for i in reversed(num1):
            carry = 0 #reset after iteration
            temp = []
            for j in reversed(num2):
                total = (ord(i) - ord('0')) * (ord(j) - ord('0')) + carry
                carry = total // 10
                rem = total % 10
                temp.append(str(rem))
            if carry:
                temp.append(str(carry))
            final_result.append(list(reversed(temp)))


        if len(final_result) > 1:
            for i in range(1,len(final_result)):
                total = len(final_result[i]) + i
                while len(final_result[i]) != total :
                    final_result[i].append('0')

        new_result = []
        for i in final_result:
            num = 0
            for j in i:
                digit = ord(j) - ord('0')  # convert character to digit
                num = num * 10 + digit
            new_result.append(num)
        
        return str(sum(new_result))


                


    

        

            
        
           