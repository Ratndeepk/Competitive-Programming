#code https://practice.geeksforgeeks.org/problems/huffman-encoding/0
#incomplete
import heapq
class Node:  
    def __init__(self, lef=None, rig=None):
        self.lef= lef
        self.rig = rig

def preorder(tree,st):
    
    if type(tree) is str:
        print(st, end=' ')
        return
    # print(type(tree),tree.lef,tree.rig,'************')

    preorder(tree.lef,st+'0')
    # print(type(tree),tree.rig,'&&&&&&&&')
    preorder(tree.rig,st+'1')
        
        
for _ in range(int(input())):
    strg = input()
    frq = list(map(int, input().split()))
    lis =[]
    for i in range(len(strg)):
        heapq.heappush(lis, (frq[i], strg[i]) )
    print(lis)
    for i in range(len(strg)-1):
        x = heapq.heappop(lis)
        y = heapq.heappop(lis)
        new = Node(x[1],y[1])
        heapq.heappush(lis,(x[0]+y[0], new))
    st=''
    # print(lis)
    preorder(lis[0][1],st)
    
    