arr = [4,3,7,8,6,2,1]
n = len(arr)
flag=True
for i in range(n-1):
    if flag:
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        flag=False
    else:
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
        flag=True
print(arr)
