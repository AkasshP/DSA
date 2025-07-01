from collections import Counter
from collections import deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = deque()
        lptr = 0
        main_freq = Counter(s1) #main_frequency window
        window_freq = Counter(window) #freequency window

        while lptr < len(s2):
            if window_freq == main_freq:
                return True

            if s2[lptr] in main_freq:
                window.append(s2[lptr])
                if s2[lptr] in window_freq:
                    window_freq[s2[lptr]] += 1 #first time initializing 
                else:
                    window_freq[s2[lptr]] = 1
                #making sure its on right track
                while window_freq[s2[lptr]] > main_freq[s2[lptr]]:
                    left = window.popleft()
                    window_freq[left] -= 1
                    if window_freq[left] == 0:
                        del window_freq[left]
            else:
                if window:
                    window.clear()
                    window_freq = {}

            lptr += 1

        if window_freq == main_freq:
            return True
        else:
            return False


                