#link https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1#
import sys
import io
import atexit


def knapSack(W, wt, val, n):
    '''
    :param W: capacity of knapsack 
    :param wt: list containing weights
    :param val: list containing corresponding values
    :param n: size of lists
    :return: Integer
    '''
    # code here
    matrix = [[0 for i in range(W+1)]for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):

            if wt[i-1] <= j and (val[i-1]+matrix[i-1][j-wt[i-1]]) > matrix[i-1][j]:
                matrix[i][j] = (val[i-1]+matrix[i-1][j-wt[i-1]])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[n][W]


#{
#  Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        print(knapSack(W, wt, val, n))
# } Driver Code Ends
