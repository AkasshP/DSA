class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(len(ransomNote),'note')
        ransom={}
        magaz={}
        ransomNote_List = list(ransomNote)
        magazine_list  = list(magazine)
        if len(ransomNote) <= len(magazine):
            check = list(set(ransomNote))
            for i in range(len(ransomNote_List)): 
                if ransom.get(ransomNote_List[i]) is None: 
                    ransom[ransomNote_List[i]] = 1
                else:
                     ransom[ransomNote_List[i]] = ransom.get(ransomNote_List[i]) + 1

            for i in range(len(magazine_list)):
                for j in range(len(check)):
                    if check[j] == magazine_list[i]:
                        if magaz.get(magazine_list[i]) is None:
                            magaz[magazine_list[i]] = 1
                        else:
                            magaz[magazine_list[i]] = magaz[magazine_list[i]] + 1       
            for i in check:
                if ransom.get(i) == magaz.get(i,0) or ransom.get(i) < magaz.get(i,0):
                    pass
                else:
                    return False
            return True

        else:
            return False
                
