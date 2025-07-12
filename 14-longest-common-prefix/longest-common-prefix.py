class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_box = []
        j = 0
        box = ""
        if len(strs):
            s = strs[0]
            if s:
                while True:
                    for i in range(len(strs)):
                        if j < len(strs[i]):
                            if box:
                                if len(strs[i]) >= 2:
                                    if strs[i][j] == box:
                                        pass
                                    else:
                                        return ''.join(prefix_box) if prefix_box else ''
                                else:
                                    if box == strs[i]:
                                        pass
                                    else:
                                        return ''.join(prefix_box) if prefix_box else ''
                            else:
                                if len(strs) >= 2:
                                    if len(strs[i]) >= 2 and j < len(strs[i]):
                                        box = strs[i][j]  #if box is empty add it
                                    else:
                                        box = strs[i]
                                else:
                                    return strs[0]
                        else:
                            return ''.join(prefix_box) if prefix_box else ''
                    
                    prefix_box.append(box)
                    box = "" #reset
                    j += 1
            else:
                return ""
        

            
            
                
