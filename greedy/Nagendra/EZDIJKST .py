# link https://www.spoj.com/problems/EZDIJKST/
for _ in range(int(input())):
    v,k = map(int, input().split())
    w = [[float('inf') for _ in range(v)] for _ in range(v)]
    for i in range(k):
        a,b,c=map(int,input().split())
        w[a-1][b-1]=c
    v1,v2 = map(int,input().split())
    v1,v2 = v1-1,v2-1
    dist=[float('inf')]*v
    dist[v1]=0
    read = [0]*v
    st=v1
    f=0
    while st !=-1:
        best=-1
        read[st]=1

        for i in range(v):
            if not read[i]:
                if dist[i]>dist[st]+w[st][i]:
                    dist[i]=dist[st]+w[st][i]
                    #print(dist)
                if best==-1 or dist[i]<dist[best]:
                    best=i
        st=best
        if st==v2 and dist[best]!=float('inf'):
            f=1
            print(dist[best])
            break
if f==0:
    print("NO")


