class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat=matrix
        # make transpose of the matrix
        for i in range(len(mat)):
            for j in range(i, len(mat)):

                # swapping mat[i][j] and mat[j][i]
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(len(mat)):
            mat[i].reverse()
        return mat