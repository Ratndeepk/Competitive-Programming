for _ in range(int(input())):
    n = int(input())
    pages=list(map(int,input().split()))
    m = int(input())
    mem = []
    ans=0
    i=0
    while i<n:
        if pages[i] not in mem:
            if len(mem)==m:
                mem.pop(0)
                mem.append(pages[i])
            else:
                mem.append(pages[i])
            ans+=1
        else:
            mem.remove(pages[i])
            mem.append(pages[i])
        i+=1
            
    print(ans)
