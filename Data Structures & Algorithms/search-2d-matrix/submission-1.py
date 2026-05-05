def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1  

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            res = binary_search(i,target)
            if res != -1:
                return True
            
        return False
