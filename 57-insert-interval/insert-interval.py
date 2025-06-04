class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        st_in = newInterval[0]
        en_in = newInterval[1]
        # start, end = intervals[0][0],intervals[0][1]
        result = []
        if intervals:
            for st , en in intervals:
                if en >= st_in:
                    if en >= en_in:
                        continue
                    else:
                        if st <= st_in:
                            result.append([st,en_in])
                        else:
                            result.append([st_in,en_in])
            print(result,'new_result')
            if result:
                mergeinterval = result + intervals
            else:
                mergeinterval = [newInterval] + intervals
            mergeinterval.sort(key=lambda x: x[0])
            new_result = []
            start , end = mergeinterval[0]
            for i,j in mergeinterval[1:]:
                print(i,j,'values')
                if end >= i:
                    if end >= j:
                        continue
                    else:
                        end = j
                else:
                    new_result.append([start,end])
                    start = i 
                    end = j
            new_result.append([start,end])
            return new_result
        else:
            return [newInterval]