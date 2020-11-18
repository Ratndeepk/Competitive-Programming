def sort012(arr,n):
    # code here
    first=0
    third =n-1 
    second=0
    while second<=third:
        if arr[second]==0:
            arr[first],arr[second]=arr[second],arr[first] 
            first+=1 
            second+=1
          
        elif arr[second]==2:
            arr[third],arr[second]=arr[second],arr[third] 
           
            third-=1 
        else:
            second+=1


arr=list(map(int,input().split()))
print(*sort012(arr,len(arr)))