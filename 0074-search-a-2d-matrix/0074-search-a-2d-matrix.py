class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl = 0
        rowr = len(matrix)-1
        while rowl<= rowr:
            rowmid = (rowl+rowr)//2
            if target > matrix[rowmid][-1]:
                rowl = rowmid+1
            elif target < matrix[rowmid][0]:
                rowr = rowmid-1
            elif matrix[rowmid][0] <= target <= matrix[rowmid][-1]:
                break 
            else:
                return False
        l,r = 0, len(matrix[0][:])-1
        while l<=r:
            mid = (l+r)//2
            if matrix[rowmid][mid] == target:
                return True
            elif target > matrix[rowmid][mid]:
                l = mid+1
            else:
                r = mid-1
        return False