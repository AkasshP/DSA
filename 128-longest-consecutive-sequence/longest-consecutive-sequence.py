class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_arr = sorted(list(set(nums))) #removed duplicates
        print(new_arr)
        # def diff(i,j):
        #     if j < len(new_arr) and i < len(new_arr):
        #         if new_arr[j] > new_arr[i]:
        #             return new_arr[j] - new_arr[i]
        #         else:
        #             return new_arr[i] - new_arr[j]
        # seq = {}
        # curr_diff = 0
        # main_diff = float(inf)
        # cnt = 0 
        # idx = 1
        # if len(new_arr) > 2:
        #     for i in range(len(new_arr)):
        #         j = i + 1
        #         curr_diff = diff(i,j)
        #         if j < len(new_arr):
        #             if main_diff == float(inf): #initially updating diff
        #                 main_diff = curr_diff
        #             if main_diff !=  curr_diff:
        #                 #new element encountered jump
        #                 main_diff = curr_diff
        #                 if main_diff == 1:
        #                     idx += 1
        #                     seq[idx] = [new_arr[i]] + [new_arr[j]]
        #             else:
        #                 #initially when you encounter a new difference then add two values
        #                 if main_diff == 1:
        #                     seq[idx] = seq.get(idx,[new_arr[i]]) + [new_arr[j]]     
        # else:
        #     if len(new_arr) == 2:
        #         return 2
        #     elif len(new_arr) == 1:
        #         return 1
        #     else:
        #         return 0
             
        # print(seq,'map')
        # if len(seq):
        #     for value in seq.values():
        #         cnt = max(cnt,len(value))
        #     return cnt
        # else:
        #     return 1

        if len(nums) > 1:
            t = new_arr[0] + 1
            max_count = 0
            cnt = 1
            for i in range(1,len(new_arr)):
                print('going inside loop')
                if t == new_arr[i]:
                    t = new_arr[i] + 1
                    cnt += 1
                else:
                    print(cnt,'cnt')
                    max_count = max(max_count,cnt)
                    cnt = 1 #reseting
                    t = new_arr[i] + 1

            max_count = max(max_count,cnt)
            return max_count
        elif len(nums) == 1:
            return 1
        else:
            return 0
                    
