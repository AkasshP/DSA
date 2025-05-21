class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if len(intervals) >= 2:
        #     st, en = intervals[0]
        #     result = []
        #     for curr_start, curr_end in intervals[1:]:
        #         if curr_start <= en:
        #             en = max(en,curr_end)
        #         else:
        #             result.append([st,en])
        #             st,en = curr_start,curr_end
        #     result.append([st,en])
        #     return result
        # If fewer than 2 intervals, nothing to merge
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        st, en = intervals[0]
        result = []

        for curr_start, curr_end in intervals[1:]:
            if curr_start <= en:
                en = max(en, curr_end)
            else:
                result.append([st, en])
                st, en = curr_start, curr_end

        result.append([st, en])
        return result