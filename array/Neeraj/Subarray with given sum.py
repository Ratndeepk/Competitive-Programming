for _ in range(int(input())):
    n,s=map(int,input()split())
    a=list(map(int,input().split()))
    cur_sum=0
    left=0
    flag=False
    for i in range(len(a)):
        cur_sum+=a[i]
        if cur_sum>=s:
            right=i
            while(s<cur_sum and left<right):
                cur_sum-=a[left]
                left+=1
            if cur_sum==s:
                print(left+1,right+1)
                flag=True
                break
    if flag==False:
        print(-1)
