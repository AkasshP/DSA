class Solution:
    def maxArea(self, height: List[int]) -> int:
        # first make sure the right pointer comes in with left pointer
        left = 0
        right = len(height) - 1
        max_area = 0
        while True:
            if left < len(height) and right >= 0:
                if height[left] < height[right]:
                    w = right - left #secret of finding width
                    h = min(height[left],height[right])
                    area = w * h
                    max_area = max(max_area, area)
                    left += 1
                else:
                    w = right - left #secret of finding width
                    h = min(height[left],height[right])
                    area = w * h
                    max_area = max(max_area, area)
                    right -= 1
                if left == right:
                    break
        return max_area
        # print(max_area,'max_area')