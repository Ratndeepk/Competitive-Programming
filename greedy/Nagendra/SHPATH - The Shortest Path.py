# link https://www.spoj.com/problems/SHPATH/
############## NZEC error

for _ in range(int(input())):
    n = int(input())
    name = {}
    l=[]
    w = [[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        name[input()] = i
        for j in range(int(input())):
            k, c = map(int, input().split())
            w[i][k-1] = c
        # print(w)
    r = int(input())
    for i in range(r):
        src, dst = input().split()
        src, dst = name[src], name[dst]

        dist = [float('inf')]*n
        dist[src] = 0
        read = [0]*n
        st = src

        while st != -1:
            best = -1
            read[st] = 1

            for i in range(n):
                if not read[i]:
                    if dist[i] > dist[st] + w[st][i]:
                        dist[i] = dist[st]+w[st][i]
                    if best == -1 or dist[i] < dist[best]:
                        best = i
            st = best
            if st == dst and dist[best] != float('inf'):
                # print(dist[st])
                l.append(dist[st])
                break
    for i in l:
        print(i)
