class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        if len(ransomNote) <= len(magazine):
            ransom={}
            magaz={}
            ransomNote_set = list(set(ransomNote))
            for i in ransomNote: 
                ransom[i] = ransom.get(i,0) + 1
            
            for i in magazine:
                magaz[i] = magaz.get(i,0) + 1  
                      
            for i in ransomNote_set:
                if ransom.get(i) == magaz.get(i,0) or ransom.get(i) < magaz.get(i,0):
                    pass
                else:
                    return False
            return True

        else:
            return False
                
