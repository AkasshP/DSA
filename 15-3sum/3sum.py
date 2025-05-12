class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute-force
        # i = 0
        # seen = set()
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         k = j + 1
        #         while k < len(nums):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 t = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 seen.add(t)
        #             k += 1
        #         j += 1
        #     i += 1
        # return [list(t) for t in seen]
        #optimized
        # nums.sort()
        # res = set()
        # for i in range(len(nums)):
        #     a = nums[i]
        #     target = -a
        #     seen = set()
        #     for j in range(i+1, len(nums)):
        #         b = nums[j]
        #         complement = target - b
        #         if complement in seen:
        #             # sort so triplet
        #             triplet = tuple(sorted((a, b, complement)))
        #             res.add(triplet)
        #         seen.add(b)

        # # convert to List[List[int]]
        # return [list(t) for t in res]
        nums.sort()                 # O(n log n)
        n = len(nums)
        res = []

        for i in range(n - 2):
            # Skip duplicate captains
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            l, r = i + 1, n - 1

            # Two‑pointer scan in O(n)
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum < target:
                    l += 1
                elif curr_sum > target:
                    r -= 1
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[l], nums[r]])

                    # Skip duplicates on the left
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Skip duplicates on the right
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    # Move both pointers inward
                    l += 1
                    r -= 1

        return res


