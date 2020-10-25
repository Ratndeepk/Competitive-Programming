str1 =  input()
str2 = input()
matrix = [[0 for i in range(len(str1)+1)]for i in range(len(str2)+1)]
index=0
for i in range(len(str1)+1):
    matrix[index][i]=i
for i in range(len(str2)+1):
    matrix[i][index]=i
    
#for i in matrix:
   # print(*i)

   
for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        
        #print(i,j)
        #print(str1[i-1],str2[j-1])
        
        if str2[i-1]==str1[j-1]:
            matrix[i][j]=matrix[i-1][j-1]
        else:
            matrix[i][j]=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1

#for i in matrix:
#    print(*i)


print(matrix[len(str2)][-1])
