def binary_search(arr,x):
    mid = len(arr)//2
    while(True):
        if mid<0 or mid>len(arr)-1:
            return -1
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr[mid+1:],x)
        else:
            return binary_search(arr[:mid],x)


element = int(input())
my_list = list(map(int,input().split()))
if binary_search(my_list,element)!=-1:
    print("Found at index:",binary_search(my_list,element))
else:
    print("Element not found")
