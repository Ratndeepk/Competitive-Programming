#link https://practice.geeksforgeeks.org/problems/common-elements1132/1#

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        a=set(A)
        b=set(B)
        c=set(C)
        lena=len(A)
        lenb = len(B)
        lenc = len(C)
        lis=[]
        for i in a:
            if (i in b) and (i in c):
                lis.append(i)
        lis.sort()
  
        return lis
        
       


#{ 
#  Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends