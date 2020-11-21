def Union(arr1, arr2, n1, n2):
    hs = set()
 
    for i in range(0, n1):
        hs.add(arr1[i])

    for i in range(0, n2):
        hs.add(arr2[i])
   
    for i in hs:
        print(i, end=" ")
   

 
 
def Intersection(arr1, arr2, n1, n2):
    hs = set()
    for i in range(0, n1):
        hs.add(arr1[i])
    
    for i in range(0, n2):
        if arr2[i] in hs:
            print(arr2[i], end=" ")
 

arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)

Union(arr1, arr2, n1, n2)
print()
Intersection(arr1, arr2, n1, n2)
print()