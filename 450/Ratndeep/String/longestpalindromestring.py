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

    st = 'aabbaaa'
    start=0 end=6 st[start]=a st[end]=a they're matching we recursive call for start-1 and end-1
    same start=1 and end=5 matches 
    start=2 and end=4 doesnt match
    jumps to step 5 start from start+1 & then end from end-1 
    we get solution in end-1 :)
    """     
                
            
for _ in range(int(input())):
    st = input()
    n = len(st)
    print(check(st,0,n-1))