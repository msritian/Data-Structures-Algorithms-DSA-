class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows=len(matrix)
        columns=len(matrix[0])
        i=0
        j=columns-1
        while(i>=0 and i<rows and j>=0 and j<columns):
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j=j-1
            else:
                i=i+1
        return False