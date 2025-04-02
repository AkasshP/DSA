class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        if len(ransomNote) <= len(magazine):
            ransom={}
            magaz={}
            ransomNote_set = list(set(ransomNote))
            for i in ransomNote: 
                if ransom.get(i) is None: 
                    ransom[i] = 1
                else:
                    ransom[i] = ransom.get(i) + 1

            for i in magazine:
                if magaz.get(i) is None:
                    magaz[i] = 1
                else:
                    magaz[i] = magaz.get(i) + 1  
                     
                
            for i in ransomNote_set:
                if ransom.get(i) == magaz.get(i,0) or ransom.get(i) < magaz.get(i,0):
                    pass
                else:
                    return False
            return True

        else:
            return False
                
