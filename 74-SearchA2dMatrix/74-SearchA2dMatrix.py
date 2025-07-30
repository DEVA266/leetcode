# Last updated: 7/30/2025, 12:24:46 PM
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        length = len(matrix[0])
        
        for i in range(len(matrix)):
            if matrix[i][length-1] >= target:
                high = length - 1
                low = 0
                mid = 0
                while low<=high:
                    mid = (high+low)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid] < target :
                        low = mid + 1
                    else :
                        high = mid - 1
           
        return False