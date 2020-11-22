#link https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

##Complete this function
import math


def maxSubArraySum(a, size):
    ##Your code here
    _max = 0
    max_ending = 0

    for i in a:
        max_ending += i
        if max_ending < 0:
            max_ending = 0
        if max_ending > _max:
            _max = max_ending
    return _max


#{
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while(T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        print(maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
