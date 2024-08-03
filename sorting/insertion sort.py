#Insertion Sort Algorithm: A simple, comparison-based sorting technique that builds the 
#final sorted array one element at a time by repeatedly inserting unsorted elements into 
#their correct position. It has a time complexity of O(n^2) and is efficient for small datasets.



arrray = list(map(int,input().split()))
n = len(array)

for i in range(1,n):
    key = arrray[i]
    j=i-1
    while j>=0 and key<arrray[j]:
        arrray[j+1]=arrray[j]
        j-=1
    arrray[j+1]=key


print(*arrray)
