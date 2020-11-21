#5 Move all negative numbers to beginning and positive to end
arr = [-12, 11,0, -5, 6, -7, 5, -3, -6]
n = len(arr)
l,r = 0,n-1
while(l<r):
    if arr[l] >= 0:
        while(r >=0 and arr[r] >= 0):
            r -= 1
        if r >= 0 and arr[r] < 0 and l < r:
            arr[l],arr[r] = arr[r],arr[l]
            l +=1
    else:
        l += 1
print("Result:",arr)