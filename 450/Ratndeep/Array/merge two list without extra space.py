#merge without using extra spce
""" 
check ith element of first array with 0th element of second array
swap if ith is greater & insert 0th element of second array in its correct position
else pass
"""
def merge(arr1, arr2, n, m): 
    p1=0
    p2=0 
    for p1 in range(n):
        if arr1[p1]>arr2[p2]:
            arr1[p1],arr2[p2]=arr2[p2],arr1[p1] 
          
         
            p3=1
            current=arr2[p2]
            while p3<m and current>arr2[p3]:
                arr2[p3-1]=arr2[p3] 
                p3+=1 
            arr2[p3-1]=current
        
        
     
    


arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
merge(arr1,arr2,len(arr1),len(arr2))

print(*arr1)
print(*arr2)