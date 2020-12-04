
#Given an array of integers where each element represents the max number
#of steps that can be made forward from that element. Write a function to 
#return the minimum number of jumps to reach the end of the array (starting 
#from the first element). If an element is 0, then cannot move through that element.
"""
Input:
2
11
1 3 5 8 9 2 6 7 6 8 9
6
1 4 3 2 6 7
Output:
3
2
"""


def min_jump(arr,n):
    if arr[0]==0:
        return -1
    jump=[float("inf")]*n 
    jump[0]=0
    for i in range(1,n):
        j=0
        while j<i:
            if j+arr[j]>=i:
                jump[i]=min(jump[i],jump[j]+1)

            j+=1
    print(jump)
    return jump[n-1]


arr = list(map(int,input().split()))
n = len(arr) 
print(min_jump(arr,n))
