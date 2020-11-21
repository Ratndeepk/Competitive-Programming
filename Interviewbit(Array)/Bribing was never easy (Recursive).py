def findcount(start,end,old,new,count):
   
    for i in range(start,end):
        if i-new.index(old[i])>0:
            new_index=new.index(old[i])
            index=i
            
            for j in range(i-1,new_index-1,-1):
                
                count[0]+=1
                old[j],old[index] = old[index],old[j]
                index=j
          
            
            print("count",count)
            if old[new_index:i+1]!=new[new_index:i+1]:
                findcount(new_index,i+1,old,new,count)
                start=i+1
        print("Old array",old)
        print("New array",new)

    return count[0]
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

if flag==0:
    print(findcount(1,len(old),old,new,[0]))
