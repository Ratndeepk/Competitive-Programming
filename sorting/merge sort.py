#Merge Sort Algorithm: A divide-and-conquer sorting technique that recursively divides the 
#list into smaller sublists, sorts them, and then merges them back together. It has a time 
#complexity of O(n log n) and is efficient for large datasets due to its stable sorting nature.

def mergesort(array):
    if len(array)>1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        mergesort(L)
        mergesort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            array[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            array[k]=R[j]
            j+=1
            k+=1

a = list(map(int,input().split()))

mergesort(a)
print(*a)
