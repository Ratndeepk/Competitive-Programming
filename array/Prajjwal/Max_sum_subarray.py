def max(A,size):
    s=0
    maxi=A[0]
    for i in range(size):
        s+= A[i]
        if s>maxi:
            maxi=s
        elif s<0:
            s=0
    return maxi
#Drivers code
A=[-2,1,-3,4,-1,2,1,-5,4]
size=len(A)
print(max(A,size))
