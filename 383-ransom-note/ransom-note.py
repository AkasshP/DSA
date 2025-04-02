class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(len(ransomNote),'note')
        ransom={}
        magaz={}
        ransomNote_List = list(ransomNote)
        if len(ransomNote) <= len(magazine):
            check = list(set(ransomNote))
            for i in range(len(ransomNote_List)): 
                if ransom.get(ransomNote_List[i]) is None: 
                    ransom[ransomNote_List[i]] = 1
                else:
                     ransom[ransomNote_List[i]] = ransom.get(ransomNote_List[i]) + 1
            print(ransom,'ransom dictionary')
            l1  = list(magazine)
            i = 0
            flag = False
            wanted = []
            unwanted = 0
            print(l1,'checking')
            while i <= len(l1) - 1:
                flag = False
                for j in range(len(check)):
                    if check[j] == l1[i]:
                        wanted.append(l1[i])
                        if magaz.get(l1[i]) is None:
                            magaz[l1[i]] = 1
                        else:
                            magaz[l1[i]] = magaz[l1[i]] + 1
                        flag = True
                if flag == False:
                    unwanted =  unwanted + 1
                i = i + 1        
            for i in check:
                if ransom.get(i) == magaz.get(i,0) or ransom.get(i) < magaz.get(i,0):
                    pass
                else:
                    return False
            return True

        else:
            return False
                
