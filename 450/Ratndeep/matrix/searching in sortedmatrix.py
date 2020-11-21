def searchMatrix(self, matrix, target):
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

target=int(input())
n = int(input()) 
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

if searchMatrix(matrix,target):
    print("Yes") 
else:
    print("no")