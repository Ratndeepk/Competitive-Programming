#User function Template for python3

def knapSack(W, wt, val, n):
    '''
    :param W: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    # code here
    mat=[[0 for i in range(W+1)] for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                mat[i][j] = max(val[i-1]+mat[i-1][j-wt[i-1]], mat[i-1][j])
            else:
                mat[i][j] = mat[i-1][j]
    return mat[n][W]
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        print(knapSack(W,wt,val,n))
# } Driver Code Ends