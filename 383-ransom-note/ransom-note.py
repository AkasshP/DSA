class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       
        if len(ransomNote) <= len(magazine):
            ransom={}
            magaz={}
            ransomNote_List = list(ransomNote)
            magazine_list  = list(magazine)
            ransomNote_set = list(set(ransomNote))
            for i in range(len(ransomNote_List)): 
                if ransom.get(ransomNote_List[i]) is None: 
                    ransom[ransomNote_List[i]] = 1
                else:
                     ransom[ransomNote_List[i]] = ransom.get(ransomNote_List[i]) + 1

            for i in magazine:
                if magaz.get(i) is None:
                    magaz[i] = 1
                else:
                    magaz[i] = magaz[i] + 1   
                
            for i in ransomNote_set:
                if ransom.get(i) == magaz.get(i,0) or ransom.get(i) < magaz.get(i,0):
                    pass
                else:
                    return False
            return True

        else:
            return False
                
