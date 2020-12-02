for _ in range(int(input())):
    n,s = map(int,input().split())
    t=""
    if s>0:
        while n>0:
            if s>=9:
                t+='9'
                s-=9
            else:
                if s==0:
                    t+='0'
                else:
                    t+=str(s)
                    s=0
            n-=1
        if n==0 and s!=0:
            print(-1)
        elif n==0 and s==0:
            print(t)
    else:
        print(-1)
