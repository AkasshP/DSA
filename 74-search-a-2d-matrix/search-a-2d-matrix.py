class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])

        def binary_search(arr):
            l = 0
            r = len(arr) - 1
            if l == r:
                if arr[0] == target: # validation before loop
                    return True
                else:
                    return False

            while l < r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            if l == r:
                    if arr[l] == target:
                        return True
                    else:
                        return False

        for i in range(len(matrix)):
            l = matrix[i][0]
            r = matrix[i][-1]

            if l <= target <= r:
                return binary_search(matrix[i])

        return False
                