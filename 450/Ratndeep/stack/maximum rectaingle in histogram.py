def max_rectaingle(arr,n):
    
    stack=[]
    i=0
    max_rec=-1
    
    """
    Example: [2,1,2,3,1] 

    * Adding values in stack till ar[i]<ar[i+1] 
    * Now pop from top of stack 
       -> if stack is empty that means arr[top]*i will be area 
       -> otherwise arr[top]*(i-stack[-1]-1) 

    1. stack=[0] 
    2. ar[0]>ar[1] 
    3. pop() 
    4. area=2*1, i=1 
    5. stack=[1,2,3] 
    6. ar[4]<arr[3] 
    7. pop()
    8. area=max(2,3*(4-2-1)) i=4 stack[top]=2 
    9. arr[4]<arr[2]
    10.area=max(3,2*(4-1-1)) i=4 stack[top]=1 
    11.stack=[4]
    12.pop()
    13.area=max(4,1*4) i=4     

    """
    while i<n:
        if stack==[] or arr[stack[-1]]<=arr[i]:
            stack.append(i) 
            i+=1
        else:
            top = stack.pop()
            if stack==[]:
                area=arr[top]*i 
                max_rec=max(max_rec,area) 
            else:
                area = arr[top]*(i-stack[-1]-1) 
                max_rec = max(area,max_rec) 

    
    while stack!=[]:
        cur = stack.pop() 
        if stack==[]:
            if max_rec<arr[cur]*i:
                max_rec=arr[cur]*i
            
        elif max_rec<arr[cur]*(i-stack[-1]-1):
            max_rec=arr[cur]*(i-stack[-1]-1) 
        
    return max_rec

    
    
arr = list(map(int,input().split()))
n = len(arr)

print(max_rectaingle(arr,n))