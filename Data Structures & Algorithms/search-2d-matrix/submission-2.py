def binarySearch(arr,target):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if binarySearch(i,target) != -1:
                return True
        return False
