for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    pre_sum=0
    new=set()
    flag=1
    for i in range(n):
        pre_sum+=arr[i]
        if pre_sum ==0 or pre_sum in new:
            flag=0
            break
        new.add(pre_sum)
    if flag==1:
        print("No")
    else:
        print("Yes")