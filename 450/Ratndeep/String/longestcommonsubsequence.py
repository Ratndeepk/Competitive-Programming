def lcs_recursion(st1,n,str2,m):
    if n==-1 or m==-1:
        return 0 

    if str1[n]==str2[m]:
        return 1+lcs_recursion(str1[:n],n-1,str2[:m],m-1) 
    return max(lcs_recursion(str1[:n],n-1,str2[:m+1],m),lcs_recursion(str1[:n+1],n,str2[:m],m-1))

    
str1 = input()
str2 = input() 
n = len(str1) 
m = len(str2) 

print(lcs_recursion(str1,n-1,str2,m-1))