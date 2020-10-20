from heapq import heapify,heappop,heappush

class minheap:
    def __init__(self):
        self.heap=[]
        heapify(self.heap)
    def add(self,x):
        heappush(self.heap,x)

    def popele(self):
        return heappop(self.heap)

for i in range(int(input())):
    heap = minheap()
    n = int(input())
    my_list = list(map(int,input().split()))

    for j in range(n):
        heap.add(my_list[j])

    k = int(input())
    for i in range(k):
        ans = heap.popele()
    print(ans)
