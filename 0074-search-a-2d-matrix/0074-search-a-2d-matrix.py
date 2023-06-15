class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if target in row:
                left = 0
                right = len(row)-1
                while left <= right:
                    mid = (right+left)//2
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        left = mid+1
                    else:
                        right = mid-1
        
        return False
