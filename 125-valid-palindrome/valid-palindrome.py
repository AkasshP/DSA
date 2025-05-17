class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer approach
        print(s,'string')
        # converteed to lowercase
        str1 = s.lower()
        # to remove all alpha non-numeric
        new_str = ''.join(ch for ch in str1 if ch.isalnum())
        l = 0 
        r = len(new_str) - 1
        while l <= r:
            if new_str[l] == new_str[r]:
                pass
            else:
                return False
            l += 1
            r -= 1
        return True
        