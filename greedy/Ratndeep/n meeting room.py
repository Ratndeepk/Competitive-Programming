for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    s = list(map(int,input().split()))
    m=[]
    for i in range(n):
        m.append([l[i],s[i]])
    m.sort(key=lambda x:x[1])
    i=0
    j=1
    
    while j<n:
        if m[i][1]<=m[j][0]:
            print(s.index(m[i][1])+1,end=" ")
            i=j
            j+=1
        else:
            j+=1
    print(s.index(m[i][1])+1,end=" ")
    print()
