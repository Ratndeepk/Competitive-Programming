def knapsack(val,wt,W,n):
    """
    Consider W=5,n=4 
    wt = [5, 3, 4, 2] 
    val = [60, 50, 70, 30] 

    So, for any value we'll consider between maximum of taking wt[i] and not taking it at all.
    taking 0 to W in column 'line 1' taking wt in rows 'line 2' 
    two cases ->
  
    * cur_wt<=total wt in that column  otherwise matrix[cur_wt][max_wt]= matrix[cur_wt-1][max_wt]  # not taking wt[cur_wt] at all 

    * take matrix[cur_wt][max_wt] = max(matrix[cur_wt-1][max_wt-wt[cur_wt]] , matrix[cur_wt-1][max_wt]) # max b/w not taking wt[cur_wt] & considering it 
    
    |   | 0   | 1   | 2           | 3            | 4            | 5               |
    | 5 | 0   | 0   | 0           | 0            | 0            | 60              |
    | 3 | ^>0 | ^>0 | ^>0         | max(0,0+50)  | 50           | max(0+50,60)=60 | 
    | 4 | ^>0 | ^>0 | ^>0         | ^50          | max(50,0+70) | max(60,0+70)    |  
    | 2 | ^>0 | ^>0 | max(0,0+30) | max(50,0+30) | max(70,0+30) | max(70,50+30)   | 

    ans = max(70,50+30)=80
    """



    matrix = [[0 for i in range(W+1)] for i in range(n)] 
    for i in range(W+1):
        if wt[0]<=i:
            matrix[0][i]=val[0] 
        else:
            matrix[0][i]=0
    for i in range(1,n):     #line 2
        for j in range(W+1):    # line 1
            if j==0:
                matrix[i][j]=0
                continue
            if j>=wt[i]:
                matrix[i][j] = max(matrix[i-1][j],matrix[i-1][j-wt[i]]+val[i])
            else:
                matrix[i][j]=matrix[i-1][j]
    
    return matrix[n-1][W]

n = int(input())
W = int(input())

val = list(map(int,input().split()))
wt = list(map(int,input().split()))
print(knapsack(val,wt,W,n))