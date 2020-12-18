#link https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1#

from sys import stdin
import math
from collections import defaultdict
#Complete this function


def majorityElement(A, N):
    #Your code here
    dic = defaultdict(int)
    for i in A:
        dic[i] += 1
        if dic[i] > N/2:
            return i

    return -1


#{
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
