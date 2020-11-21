arr=list(map(int,input().split()))
d=dict.fromkeys(range(1,len(arr)+1),0)
for i in arr:
    if (i in d):
       d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if d[k]>1:
        rep=k
    if d[k]==0:
        mis=k
print(rep,mis)   
        
    
    
 