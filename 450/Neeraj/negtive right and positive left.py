arr=list(map(int,input().split()))
left=0
right=len(arr)-1
while(left<=right):
    #print(left)
    #print(right)
    if arr[left]<0 and arr[right]<0:
        left+=1
    elif arr[left]>0 and arr[right]<0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    elif arr[left]>0 and arr[right]>0:
        right-=1
    else:
        left+=1
        right-=1
print(arr)
