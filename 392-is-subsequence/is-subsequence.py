from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = Counter(s)
        s2 = Counter(t)
        keys = [i for i in s1.keys()]
        flag = True
        for i in keys:
            if i in [i for i in s2.keys()] :
                pass
            else:
                flag = False
        #1st level of screening no character found then return False directly don't wanna check the sequence
        if flag:
            list_t = list(t)
            list_s = list(s)
            def seq(l,k,s1):
                if all(value == 0 for value in s1.values()):
                    return True
                for i in range(l,len(list_s)):
                    for j in range(k,len(list_t)):
                        if list_s[i] == list_t[j]:
                            s1[list_s[i]] -= 1
                            return seq(i+1,j+1,s1) #forward the pointer and check next elements matches
                        elif list_t[j] == list_s[0]:
                            s1 = Counter(s) #reset the counter and restart it again reducing the value
                            s1[list_s[0]] -= 1
                            return seq(1,j+1,s1) #found the new starting sequence
   
                    return False #suppose the whole loop runs no matches found not even starting or sequence match then end it
            
            return seq(0,0,s1)
            
        else:
            return flag

                            


