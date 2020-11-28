#link https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False

        for i in matrix:
            if i[m-1] >= target:
                for j in i:
                    if j == target:
                        return True
                return False
        return False
