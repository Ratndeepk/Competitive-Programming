class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix!=[]:
            m = len(matrix[0])
            n = len(matrix)
            for i in matrix:
                if i!=[]:
                    if target<=i[-1]:
                        for j in i:
                            if target==j:
                                return True
                        return False
                else:
                    return False
        return False
