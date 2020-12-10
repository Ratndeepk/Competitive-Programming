#link https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
def maximumMeetings(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    # code here
    meetg = []
    
    for i in range(n):
        temp=[]
        temp.append(start[i])
        temp.append(end[i])
        meetg.append(temp)
        temp.append(i+1)
    
    meetg.sort(key = lambda x: x[1])
    sdl =[]
    c=1
    finish = meetg[0][1]
    sdl.append(meetg[0][2])
    for i in range(1,n):
        if finish < meetg[i][0]:
            c+=1
            finish = meetg[i][1]
            sdl.append(meetg[i][2])
    print(*sdl)
    return sdl
    



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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        maximumMeetings(n,start,end)
# } Driver Code Ends