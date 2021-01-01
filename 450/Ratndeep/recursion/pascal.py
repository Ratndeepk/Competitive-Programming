def pascal(n):
    if n==0:
        return [] 
    if n==1:
        return [[1]] 
    new_row=[1] 
    result = pascal(n-1) 
    last_row=result[-1] 
    for i in range((len(last_row)-1)):
        new_row.append(last_row[i]+last_row[i+1]) 
    new_row.append(1) 
    result.append(new_row) 
    return result
    
    
    
n = int(input()) 
a = pascal(n) 
print(a[n-1])