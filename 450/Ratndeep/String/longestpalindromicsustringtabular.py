def check(n,st,tab):
    maxlps=1
    for i in range(n-2,-1,-1):
        
        for j in range(i+1,n):
           
            if st[i]==st[j]:
              
                
                """
                at i=1 j=3 st[1]==st[3] 
                
                    a     b       c      b
                a|True | False| False| False |
                b|False| True | False| True  |
                c|False| False| True | False |
                b|False| False| False| True  |

                Now, we will check that between st[1] and s[3] things are palindrome 
                simply by checking st[2]==st[2] 

                at s[0]==s[3] 
                will check s[1] & s[2] which are not equal thus rejected
                """
                start,end,flag=i+1,j-1,0
                if j-i==1 or tab[i+1][j-1]:
                    tab[i][j]=True 
                    maxlps = max(maxlps,j-i+1)  # j-i+1 gives length of current palindrome substring example 'abcb' (i=1 j=3)  length=j-i+1=3
          
          
    return maxlps
    

for _ in range(int(input())):
    st = input() 
    n = len(st) 
    tab = [[False for i in range(n)] for i in range(n)] 
    for i in range(n):
        tab[i][i]=True 

    """
    Example: 
    st = 'abcb'
        a     b       c      b
    a|True | False| False| False |
    b|False| True | False| False |
    c|False| False| True | False |
    b|False| False| False| True  |

    """
    print(check(n,st,tab))


# Below code will generate the maximum palindrome substring
    def check(n,st,tab):
    maxlps=1
    sol=st[0]
    for i in range(n-2,-1,-1):
        
        for j in range(i+1,n):
           
            if st[i]==st[j]:
                start,end,flag=i+1,j-1,0
                if j-i==1 or tab[i+1][j-1]:
                    tab[i][j]=True 
                    if maxlps<=j-i+1:
                        sol=st[i:j+1]
                        maxlps=j-i+1
                    #maxlps = max(maxlps,j-i+1)  # j-i+1 gives length of current palindrome substring example 'abcb' (i=1 j=3)  length=j-i+1=3
          
          
    return sol
    

for _ in range(int(input())):
    st = input() 
    n = len(st) 
    tab = [[False for i in range(n)] for i in range(n)] 
    for i in range(n):
        tab[i][i]=True 
    print(check(n,st,tab))