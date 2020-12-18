#link https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
import heapq
def minCost(a,n) :
    '''
    use heapq module , imported already by driver code.
    :param a: given array
    :param n: size of array
    :return: Integer
    '''
    # code here
    heapq.heapify(a)
    max=0
    
    for i in range(n-1):
        rope1 = heapq.heappop(a)
        rope2 = heapq.heappop(a)
        max+=(rope1+rope2)
        heapq.heappush(a,rope1+rope2)
    return max



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict
# Contributed by : Nagendra 

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(minCost(a,n))
# } Driver Code Ends