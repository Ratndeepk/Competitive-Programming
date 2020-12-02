#Complexity O(m*n)

def lcs(str1,n,str2,m):
    matrix = [[0 for i in range(n+1)] for i in range(m+1)] 

    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[j-1]==str2[i-1]:
                matrix[i][j] = 1+matrix[i-1][j-1]    # if equal then exculde both character and add 1 to last value without both values
            else:
                matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])  # if not equal take max of exculding once both character

    return matrix[m][n]

str1 = input()
str2 = input() 
n = len(str1) 
m = len(str2) 

print(lcs(str1,n,str2,m))

"""
lcs('aab','azb')  ->      1+lcs('aa','az')  -> 1+1=2 
                        /                 \
                max(lcs('a','az')    ,      lcs('aa','a')) -> 1+lcs('a','') ->1+0
                 /          \                             
        max(lcs('','az'),lcs('a','a'))  -> max(0,1)             
"""