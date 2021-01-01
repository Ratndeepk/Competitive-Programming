#Uhttps://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    # code here
    arr.sort()
    dep.sort()
    c=1
    maxx=1
    i, j =1, 0
    
    while i<n and j<n:
        if arr[i]<=dep[j]:
            c+=1
            if c>maxx:
                maxx=c
            i+=1
        else:
            c-=1
            j+=1
        
                
            
    return maxx
            
            
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(str,input().strip().split()))
        departure = list(map(str,input().strip().split()))
        print(minimumPlatform(n,arrival,departure))
# } Driver Code Ends