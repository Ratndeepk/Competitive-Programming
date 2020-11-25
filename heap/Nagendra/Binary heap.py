class MaxHeap:

    def __init__(self,max_size):
        self.max_size = max_size
        self.heap = [-1]*max_size
        self.heap_size = 0

    def heapify(self,i):

        left = 2*i+1
        right = 2*i+2
        #print(self.heap)

        if left < self.heap_size and self.heap[i] < self.heap[left]:
            largest = left
        else:
            largest = i

        if right < self.heap_size and self.heap[largest] < self.heap[right]:
            largest = right
            
        if largest !=i:
            self.heap[i],self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)


    def insert(self,value):

        if self.max_size > self.heap_size:
            self.heap_size +=1
            self.heap[self.heap_size-1] =value
            i=self.heap_size-1
            #print(self.heap,i//2)
            while self.heap[i//2] < self.heap[i]:
                self.heap[i//2],self.heap[i] = self.heap[i],self.heap[i//2]
                i//=2
            #print(self.heap)
        else:
            print('***********Overflow*************')


    def del_max(self):

        if self.heap_size ==0:
            print('Underflow')
        else:
            print(self.heap[0],'is deleted')
            self.heap[0],self.heap[self.heap_size-1] = self.heap[self.heap_size-1], self.heap[0]
            self.heap_size-=1
            self.heapify(0)


    def increase_key(self,key,i):

        if key < self.heap[i]:
            print("key is lesser than current value")
        else:
            self.heap[i]=key

            while self.heap[i//2] < key :
                self.heap[i//2],self.heap[i] = self.heap[i],self.heap[i//2]
                i//=2

    def traverse(self):

        for i in range(self.heap_size):
            print(self.heap[i],end=' ')
        print()
    
    def heap_sort(self):
        
        for i in range(self.heap_size,1,-1):
            self.heap[0],self.heap[self.heap_size-1] = self.heap[self.heap_size-1],self.heap[0]
            self.heap_size -=1
            self.heapify(0)

    

minHeap = MaxHeap(15) 
minHeap.insert(5) 
minHeap.insert(3) 
minHeap.insert(17) 
minHeap.insert(10) 
minHeap.insert(84) 
minHeap.insert(19) 
minHeap.insert(6) 
minHeap.insert(22) 
minHeap.insert(9) 
minHeap.traverse()
minHeap.increase_key(100,5)
minHeap.traverse()
minHeap.del_max()
minHeap.traverse()
minHeap.heap_sort()
print(minHeap.heap)