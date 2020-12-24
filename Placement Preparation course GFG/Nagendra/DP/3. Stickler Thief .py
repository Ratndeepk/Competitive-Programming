#User function Template for python3

def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    # code here
    arr = [0 for i in range(n+1)]

    for i in range(1,n+1):
        arr[i]= max(a[i-1]+arr[i-2], arr[i-1])
    # if n<=0:
    #     return 0
    
    # return max(a[n-1] + FindMaxSum(a,n-2), FindMaxSum(a,n-1))
    # print(arr)

    return arr[n]

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
        a = list(map(int,input().strip().split()))
        print(FindMaxSum(a,n))
# } Driver Code Ends  

