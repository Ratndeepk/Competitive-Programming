# Time Complexity O(n*m)
"""
Given a binary matrix. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Example 1:

Input:
n = 4, m = 4
M[][] = {{0 1 1 0},
         {1 1 1 1},
         {1 1 1 1},
         {1 1 0 0}}
Output: 8
Explanation: For the above test case the
matrix will look like
0 1 1 0
1 1 1 1
1 1 1 1
1 1 0 0
the max size rectangle is 
1 1 1 1
1 1 1 1
and area is 4 *2 = 8.
"""

row,col = map(int,input().split())
matrix=[] 
for i in range(row):
    matrix.append(list(map(int,input().split())))

cur_row = [0]*col 
maxarea=-1
for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            cur_row[j]=0 
        else:
            cur_row[j]+=1 
    
    # Same as maxrec in histogram
    # but for every addition of row in matrix
    stack=[]
    s=0
    while s<m:
        if stack==[] or cur_row[stack[-1]]<=cur_row[s]:
            stack.append(s)
            s+=1 
        else:
            top=stack.pop() 
            if stack==[]:
                maxarea=max(maxarea,cur_row[top]*s) 
            else:
                maxarea=max(maxarea,cur_row[top]*(s-stack[-1]-1)) 

    while stack:
        top=stack.pop()
        if stack==[]:
            maxarea=max(maxarea,cur_row[top]*s) 
        else:
            maxarea=max(maxarea,cur_row[top]*(s-stack[-1]-1)) 

print(maxarea)
