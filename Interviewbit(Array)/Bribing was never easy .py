
new = list(map(int,input().split()))
coin = list(map(int,input().split()))
flag=0
count=0
n=len(new)
old = [i for i in range(1,n+1)]
for i in range(n):
    if i-new.index(old[i])>coin[i]:
        flag=1
        break


if flag==1:
    print(-1)
else:
    diff = []
    
    for i in range(n):
            diff.append(i-new.index(old[i]))
    for i in range(n):
        if diff[i]==0:
            diff[i]=float("-inf")
    print("diff",diff)
    print("Old array",old)
    print("New array",new)
    while old!=new:
        for i in range(1,len(old)):
            if diff[i]>0:
                new_index=new.index(old[i])
                index=i
                for j in range(i-1,new_index-1,-1):
                    old[j],old[index] = old[index],old[j]
                    index=j
                    count+=1    
                print("count",count)
                break
            diff[i]=float("-inf")
            
        for i in range(n):
            diff[i]=(i-new.index(old[i]))
        for i in range(n):
            if diff[i]==0:
                diff[i]=float("-inf")
        print("diff",diff)
        print("Old array",old)
        print("New array",new)
            
    print(count)
