#link https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

def JobScheduling(Jobs,n):
    '''
    :param Jobs: list of "Job" class defined in driver code, with "profit" and "deadline".
    :param n: total number of jobs
    :return: A list of size 2 having list[0] = count of jobs and list[1] = max profit
    '''
    '''
    {
        class Job:.
        def __init__(self,profit=0,deadline=0):
            self.profit = profit
            self.deadline = deadline
            self.id = 0
    }
    '''
    # code here
    maxx, c = 0, 0
    Jobs.sort(key=lambda x : x.profit,reverse=True)
    sdl =set()
    
    for i in Jobs:
        temp=i.deadline-1
        while temp>=0 :
            if temp not in sdl:
                c+=1
                sdl.add(temp)
                maxx+=i.profit
                break
            temp-=1
    return [c,maxx]


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        res = JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends