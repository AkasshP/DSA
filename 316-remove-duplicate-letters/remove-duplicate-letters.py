class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        for i in s:
            if i not in st:
                st.append(i)
        occurence = {}
        main_window = []

        for idx, ch in enumerate(s):
            if ch in st:
                occurence[ch] = idx

        j = 0
        while occurence:
            early = min(occurence.values())
            window = s[j:early+1]
            candidates = [ch for ch in window if ch in occurence]
            char = min(candidates)
            main_window.append(char)
            window.index(char)
            if char in occurence:
                del occurence[char]
            j = j +  window.index(char) + 1 #now its the starting point

        return ''.join(main_window)
