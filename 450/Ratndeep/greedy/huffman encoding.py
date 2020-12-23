"""
Huffman Encoding

https://www.youtube.com/watch?v=co4_ahEDCho&t=928s&ab_channel=AbdulBari

"""

from heapq import heapify,heappop,heappush

class Node:
    def __init__(self,data,freq,left,right):
        self.data=data
        self.frq=freq 
        self.left=left 
        self.right=right 

    def __lt__(self,other):
        return self.freq<other.freq 

def print_data(root,strs):
    if root==None:
        return 
    if root.data!=None:
        print(strs,end=" ") 
    if root.left:
        strs+="0" 
        print_data(root.left,strs) 
        strs=strs[:len(strs)-1] 
    if root.right:
        strs+="1" 
        print_data(root.right,strs) 
        strs=strs[:len(strs)-1] 
        
for _ in range(int(input())):
    string=input() 
    freq = list(map(int,input().split()))
    n = len(string)
    heap=[] 
    for i in range(n):
        heappush(heap,Node(string[i],freq[i],None,None)) 
    while len(heap)>1:
        v1 = heappop(heap)
        v2 = heappop(heap) 

        v3 = Node(None,v1.freq+v2.freq,v1,v2) 
        heappush(heap,v3) 

    