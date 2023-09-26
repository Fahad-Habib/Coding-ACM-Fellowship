class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        for row in matrix:
            if row[-1] >= target and row[0] <= target:
                if target in row:
                    return True
        return False
