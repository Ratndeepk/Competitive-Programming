n,h = map(int,input().split())
stack = list(map(int,input().split()))
command = list(map(int,input().split()))
index=0
flag=0
for i in command:
    if i==0:
        break
    elif i==1:
        if index!=0:
            index-=1
    elif i==2:
        if index!=n-1:
            index+=1
    elif i==3:
        if flag==0:
            if stack[index]>0:
                flag=1
                stack[index]-=1
            
    elif i==4:
        if flag==1:
            if stack[index]<h:
                stack[index]+=1
                flag=0
print(*stack)
