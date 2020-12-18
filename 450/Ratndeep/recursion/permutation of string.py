"""
Permutation of String 
https://www.youtube.com/watch?v=GuTPwotSdYw&ab_channel=TECHDOSE

Example - ABC

ABC 
-> swap A with A (ABC) 
-> swap A with B (BAC) 
-> swap A with C (CBA) 

* Fixing first value because we already swapped it* 

ABC 
-> swap B with B (ABC) 
-> swap B with C (ACB) 

BAC 
-> swap A with A (BAC) 
-> swap A with C (BCA) 

CBA
-> swap B with B (CBA) 
-> swap B with A (CAB) 

* fixing first two values because we already swapped it* 

--Only one value left recursion break here-- 

Answer - ABC,ACB,BAC,BCA,CBA,CAB 

"""
def tostring(st):
    return "".join(st) 

def permutation(st,a,b,sol):
    if a==b:
        sol.append(tostring(st))
    
    for i in range(a,b+1):
        st[a],st[i]=st[i],st[a] 
        permutation(st,a+1,b,sol) 
        st[a],st[i]=st[i],st[a]   #backtracking

    

string = list(input()) 
sol=[]
permutation(string,0,len(string)-1,sol)
print(*sol)