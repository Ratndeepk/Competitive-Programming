from heapq import heappush,heappop,heapify

# heappop -> pop and return the smallest element from heap 
# heappush -> push the value item onto the heap, maintaining heap invarient 
# heapify -> transform list into heap, in place, in linear time

class Minheap:
    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return (i-1)//2

    def insertkey(self,k):
        heappush(self.heap,k)


    #modifying heap[i] to new value
    # new value is considered smaller than heap[i]
    def decreasekey(self,i,new_val):
        self.heap[i]=new_val
        while i!=0 and self.heap[self.parent(i)]>self.heap[i]:
            #simple swap
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    #remove min element from heap
    def extractmin(self):
        return heappop(self.heap)

    #function to delete key at index i
    def deletekey(self,i):
        self.decreasekey(i,float(-"inf"))
        self.extractmin()

    def getmin(self):
        return self.heap[0]

h = Minheap()
h.insertkey(3)
h.insertkey(2)
h.insertkey(1)
h.insertkey(15)

h.insertkey(5)
h.insertkey(4)

h.insertkey(45)

print(h.extractmin())

print(h.getmin())

h.decreasekey(2,1)
print(h.getmin())

