#User function Template for python3

def rotateArr(A,D,N):
    #Your code here
    # for i in range(D):
    #     A[i],A[N-D+i] = A[N-D+i], A[i]
    # left, right = 0,N-1-D
    # while left < right:
    #     A[left], A[right] = A[right], A[left]
    #     left+=1
    #     right-=1
        
        #naive
    one = A[:D]
    two = A[D:]
    for i in range(len(two)):
        A[i]=two[i]
    i=len(two)
    for j in range(len(one)):
        A[j+i]=one[j]



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        
        rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends