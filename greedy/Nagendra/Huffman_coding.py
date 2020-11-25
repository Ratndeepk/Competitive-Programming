#link https://practice.geeksforgeeks.org/problems/huffman-encoding/0
import math

class MinHeap:

    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = []
        self.heap_size = 0

    def heapify(self, index):

        lt = index*2+1
        rt = index*2+2
        #print(self.heap)
        if lt < self.heap_size and self.heap[lt][1] < self.heap[index][1]:
            min_index = lt
        else:
            min_index = index
        if rt < self.heap_size and self.heap[rt][1] < self.heap[min_index][1]:
            min_index = rt
        if min_index != index:
            self.heap[index][0], self.heap[min_index][0], self.heap[index][1], self.heap[min_index][
                1] = self.heap[min_index][0], self.heap[index][0], self.heap[min_index][1], self.heap[index][1]
            self.heapify(min_index)

    def insert(self, value, ch):
        t = []
        t.append(ch)
        t.append(value)
        self.heap.append(t)
        #print(self.heap)
        if self.heap_size > 0:
            temp = self.heap_size
            p = math.ceil(temp/2)-1
            print(value, p, self.heap_size)
            while(self.heap[temp][1] < self.heap[p][1] and temp>0 and p>-1):
                print(value,p,self.heap_size)
                parent = math.ceil(temp/2)-1
                self.heap[temp][0],self.heap[parent][0]=self.heap[parent][0],self.heap[temp][0]
                self.heap[temp][1], self.heap[parent][1] = self.heap[parent][1], self.heap[temp][1]
                temp = math.ceil(temp/2)-1
                p = math.ceil(temp/2)-1
                # print(self.heap)

        self.heap_size += 1

    def extract_mean(self):
        self.heap[0][0], self.heap[0][1], self.heap[self.heap_size - 1][0], self.heap[self.heap_size -
                                                                                      1][1] = self.heap[self.heap_size-1][0], self.heap[self.heap_size-1][1], self.heap[0][0], self.heap[0][1]
        #print(self.heap)
        t_c = self.heap[self.heap_size-1][0]
        t_v = self.heap[self.heap_size-1][1]
        self.heap.pop()
        self.heap_size -= 1
        #print(self.heap)
        self.heapify(0)
        #print(self.heap)
        return (t_c, t_v)


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)


def huffman_encoding(node, left=True, string=''):
    if type(node) is str:
        print(string, end=' ')
        return {node: string}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_encoding(l, True, string+'0'))
    d.update(huffman_encoding(r, False, string+'1'))

    return d


for _ in range(int(input())):
    char = input()
    fre = list(map(int, input().split()))

    heap = MinHeap(len(char))
    for i in range(len(char)):
        heap.insert(fre[i], char[i])
    print(heap.heap)
    for i in range(len(char)-1):
        (k1, c1) = heap.extract_mean()
        (k2, c2) = heap.extract_mean()
        node = Node(k1, k2)
        print(heap.heap)
        print()
        heap.insert(c1+c2, node)
        print(heap.heap)
        print()
    

    code = huffman_encoding(node)
    print()
    # #print(code)
    # for i in char:
    #     #print(i)
    #     print(code[i], end=' ')
    # print()
