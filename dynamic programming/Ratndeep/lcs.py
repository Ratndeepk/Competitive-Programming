str1 = input()
str2 = input()
matrix = [[0 for i in range(len(str1)+1)]for i in range(len(str2)+1)]


for i in range(len(str2)):
    for j in range(len(str1)):
        if str1[j]==str2[i]:
            matrix[i+1][j+1]=1+matrix[i][j]
        else:
            matrix[i+1][j+1]=max(matrix[i+1][j],matrix[i][j+1])

print(matrix[len(str2)][-1])
