#Longest Palindromic Substring Recursive Solution
def check(st,start,end):
    if start>end: # means no palindromic string exists
        return 0
    if start==end: # base case 
        return 1 
    
    if st[start]==st[end]:                      # if start and end matches we'll check for start+1 and end-1 
        remaining = end-start-1                 # ex- 'abba' a->a remaining= 4-1-1=2
        if remaining==check(st,start+1,end-1):           
            return 2+remaining 

    return max(check(st,start+1,end),check(st,start,end-1))  #step 5 if first character doesn't matches then start+1 and vice versa
    
    """
    Example: 

    st='abdbca' 
                
                       abdbca   ans=3
                          |
                       3[bdbc]
                        /   \
            max(3[2+bdb]  1[dbc])
                  /          /    \
               1[d]    max(1[db]   1[bc])
                        /   \       /  \
                 max[1[d]  1[b]]  max(1[b]  1[c])
            
    """     
                
            
for _ in range(int(input())):
    st = input()
    n = len(st)
    print(check(st,0,n-1))