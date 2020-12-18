def check(n,arr):
    index=0
    ar = [0]*(2*n+1) 
    for i in range(n):
        if i%2==0:
            ar[i]=arr[index] 
        else:
            ar[i]="$" 
        index+=1 

    temp = [0]*len(ar) 
    start,end=0,0 

    for i in range(len(ar)):
        while(start>0 and end<len(ar)-1 and ar[start-1]==ar[end+1]):
            start-=1
            end+=1 
        temp[i]=end-start+1 

        if end==len(temp)-1:
            break 
        if i%2==0:
            newcenter=end+1 
        else:
            newcenter=end 

        for j in range(i+1,end+1):
            temp[j] = min(temp[i-(j-i)],2*(end-j)+1) 

            if j+temp[i-(j-i)]//2==end:
                newcenter=j
                break 
        i=newcenter
        end=i+temp[i]//2 
        start=i-temp[i]//2 

        maximum = float("-inf") 
    for i in range(len(temp)):
        val=temp[i]//2 
        if maximum<val:
            maximum=val 
    return maximum 

st = input()
n=len(st) 
print(check(n,st))
