#Selection Sort Algorithm: A simple, comparison-based sorting technique that repeatedly selects 
#the smallest (or largest) element from the unsorted portion and swaps it with the first unsorted 
#element. It has a time complexity of O(n^2) and is inefficient for large datasets but easy to implement.


array = list(map(int,input().split()))
n = len(array)
i=0
#sorted array
while i<n:

    #find minimum element in unsorted array
    temp=i
    for j in range(i+1,n):
        if array[temp]<array[j]:
            temp=j
    #swap cuurent element with minimum element in unsorted array
    array[i],array[temp]=array[temp],array[i]
    i+=1


print(array)
