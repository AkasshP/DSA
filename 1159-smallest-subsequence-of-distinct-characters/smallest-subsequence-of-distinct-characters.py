class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # visited = set()
        # position = {}
        # for i,j in enumerate(s):
        #     if j not in visited:
        #         visited.add(j)
        #         position[j] = i

        # main_box = []
        # backward_box = []
        # # going forward
        # def lexf(arr):
        #     if not visited or not arr:
        #         return main_box
        #     for idx,ch in enumerate(arr):
        #         if main_box[-1] < ch and ch in visited: # and we have to see position like ith == position
        #             main_box.append(ch)
        #             visited.remove(ch)
        #             lexf(arr[idx+1:])
        #             break
        #         else:
        #             if ch in visited:
        #                 main_box.append(ch)
        #                 visited.remove(ch)
        #                 lexf(arr[idx+1:])
        #                 break
        # def lexb(arr):
        #     if not visited or not arr:
        #         return backward_box

        #     for i in arr:
        #         if i in visited:
        #             backward_box.append(i)
        #             visited.remove(i)
            
        # if s:
        #     char = min(s)
        #     main_box.append(char)
        #     visited.remove(char)
        #     idx = s.index(char)
        #     window_forward = s[idx+1:]
        #     window_backward = s[:idx]
        #     lexf(window_forward)
        #     # no backward window then
        #     if window_backward:
        #         lexb(window_backward)
        #     if not backward_box:
        #         return ''.join(main_box)
        #     else:
        #         return ''.join(backward_box) + ''.join(main_box)
        stack = []
        visited = set()
        position = {c: i for i,c in enumerate(s)}
        for i,j in enumerate(s):
            if j in visited:
                continue
            while stack and j < stack[-1] and position[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(j)
            visited.add(j)
        return ''.join(stack)







            
