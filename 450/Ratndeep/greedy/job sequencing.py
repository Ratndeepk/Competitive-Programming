"""
Job Sequencing 
https://www.youtube.com/watch?v=zPtI8q9gvX8&t=608s&ab_channel=AbdulBari

Given a set of N jobs where each job i has a deadline and profit 
associated to it. Each job takes 1 unit of time to complete and 
only one job can be scheduled at a time. We earn the profit if 
and only if the job is completed by its deadline. The task is to 
find the maximum profit and the number of jobs done.

"""

def job_seq(id,deadlines,profit,n):
    
    d_profit = [] 
    for i in range(n):
        d_profit.append([id[i],deadlines[i],profit[i]]) 

    d_profit.sort(key=lambda x:x[2],reverse=True) 
    ans=0
    positions = [False]*n 
    for i in range(n):
        if positions[i]==False:
            positions[i]=True 
            ans+=d_profit[i][2] 
        else:
            pointer=i 
            flag=False
            while positions[pointer]:
                pointer-=1 
                if pointer==-1:
                    flag=True 
                    break  
            if flag:
                continue 
            else:
                poisitions[pointer]=True 
                ans+=d_pofit[i][2] 

    return ans 

id = input().split() 
deadlines = list(map(int,input().split()))
profit = list(map(int,input().split())) 

print(job_seq(id,deadlines,profit,len(profit))) 
