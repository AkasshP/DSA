class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_freq = {}
        #last elements of all those characters
        for i in range(len(s)):
            if max_freq.get(s[i]):
                max_freq[s[i]] = i
            else:
                max_freq[s[i]] = i
        # print(max_freq,'max_freq')

        current_max = max_freq[s[0]]
        new_str = []
        main_str = []
        i = 0
        while i < len(s):
            while i <= current_max and i < len(s):
                if current_max >= max_freq[s[i]]:
                    new_str.append(s[i])
                else:
                    current_max = max(current_max,max_freq[s[i]])
                    new_str.append(s[i])
                i += 1
            if i < len(s):
                current_max = max(current_max,max_freq[s[i]])
                main_str.append(len(new_str))
                new_str.clear()#reset
                new_str.append(s[i])#add the new element
            i += 1
        if new_str:
            main_str.append(len(new_str))
        
        return main_str


            


         