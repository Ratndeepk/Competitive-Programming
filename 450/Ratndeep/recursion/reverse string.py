def reverse(s,i,n,so):
    if i==n:
        return 
    
    reverse(s,i+1,n,so)
    so.append(s[i])

s = input() 
so=[]
reverse(s,0,len(s),so)
print(so)