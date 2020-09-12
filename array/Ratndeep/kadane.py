#code
for _ in range(int(input())):
    n=int(input())
    l = list(map(int,input().split()))
    f_sum=0
    c_sum=0
    for i in range(n):
        c_sum+=l[i]
        if c_sum<0:
            c_sum=0
        
        elif c_sum>f_sum:
            f_sum=c_sum
        
    if f_sum==0:
        print(max(l))
    else:
        print(f_sum)


#ratndeep
#https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
#O(n)
