class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for num in row:
                if num == target:
                    return True
                if num > target:
                    break
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(arr, t):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] == t:
                    return True
                if arr[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        for row in matrix:
            if bs(row, target):
                return True
        return False

