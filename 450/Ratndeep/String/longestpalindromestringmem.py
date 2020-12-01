#Longest Palindromic Substring DP Memorization Solution
"""

    st='abcb' 
                        (0,3)
                         abcb   ans=3
              (1,3)    /     \ (0,2)
            max(3[2+bcb]      1[abc])
                  /          /        \
           (2,2)1[c]   (0,1)        (1,2)
                      max(1[ab]     1[bc]) 
                        /   \       /     \
                     (0,0)  (1,1)  (1,1)   (2,2)
                 max[1[a]  1[b]]  max(1[b]  1[c])

using memorization we don't have to calculate (1,1) two times 
  Initial-
      a    b    c    b
   a|None|None|None|None|
   b|None|None|None|None|
   c|None|None|None|None|
   b|None|None|None|None|

   calculating [0,3] s[0]!=s[3] (call-[1,3] and [0,2]) 
   * [1,3]  s[1]==s[3]  (call [2,2]) returns 1 
     [1,3] = 2+1=3 
   
   * [0,2] s[0]!=s[2] (calls [1,2] & [0,1]) and so on. 

   Final matrix will look like:

      a    b    c    b
   a|None|  1 | 1  | 3  |
   b|None|None| 1  |None|
   c|None|None|None|None|
   b|None|None|None|None|
   
   ans = a[0][3]
"""
def check(st,start,end,mem):
    if start>end: # means no palindromic string exists
        return 0
    if start==end: # base case 
        return 1 
    
    if mem[start][end]==None:  
        if st[start]==st[end]:
            remaining = end-start-1                
            if remaining==check(st,start+1,end-1,mem):           
                return 2+remaining 
        

        mem[start][end]=max(check(st,start+1,end,mem),check(st,start,end-1,mem))
        
    return mem[start][end]  
    
        
            
for _ in range(int(input())):
    st = input()
    n = len(st)
    mem = [[None for i in range(n)] for i in range(n)]
    check(st,0,n-1,mem)
    for i in mem:
        print(*i)
    print(mem[0][n-1])
    
   