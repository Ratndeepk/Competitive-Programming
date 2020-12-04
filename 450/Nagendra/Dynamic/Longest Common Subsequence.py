#link https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1#
import sys
import io
import atexit


def lcs(m, n, X, Y):
    '''
    :param m: length of string X 
    :param n: length of string Y
    :param X: string X
    :param Y: string Y
    :return: Integer
    '''
    # code here
    matrix = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                matrix[i][j] = 1+matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[m][n]


#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m, n = map(int, input().strip().split())
        X = str(input())
        Y = str(input())
        print(lcs(m, n, X, Y))
# } Driver Code Ends
