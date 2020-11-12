def JobScheduling(Jobs,n):

    res,count = 0,0
    Jobs = sorted(Jobs , key = lambda x: x.profit, reverse=True)
   
    result = [0 for i in range(n)]
    
    slot = [False for i in range(n)]

    for i in range(n):
        
        for j in range(min(n,Jobs[i].deadline)-1,-1,-1):
       
            if not slot[j]:
                
                result[j] = i
                slot[j] = True 
                break

    for i in range(n):
        if slot[i]:
            res+=Jobs[result[i]].profit
            count+=1

    ans = []
    ans.append (count)
    ans.append (res)
    return ans