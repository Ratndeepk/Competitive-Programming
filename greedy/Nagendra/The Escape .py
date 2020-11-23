# https://www.codechef.com/problems/REN2013G

def dis(f,s):
    return ((f[0]-s[0])**2+(f[1]-s[1])**2)

n = int(input())
cord=[[0,0]]
for i in range(n+1):
    x,y=map(int,input().split())
    cord.append([x,y])

dist = [float('inf')]*(n+2)
dist[0]=0
read=[0]*(n+2)
s=0

while s!=-1:
    read[s]=1
    best=-1

    for k in range(n+2):
        if not read[k]:
            if dist[k]>dist[s]+dis(cord[s],cord[k]):
                dist[k]=dist[s]+dis(cord[s],cord[k])
            if best==-1 or dist[k] < dist[best]:
                best=k
    s = best
    if s==n+1:
        break
print(dist[n+1])





