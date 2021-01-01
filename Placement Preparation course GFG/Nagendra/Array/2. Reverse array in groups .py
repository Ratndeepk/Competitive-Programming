#link https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1/?track=ppc-arrays&batchId=221#

class Solution:	
	def reverseInGroups(self, arr, N, K):
		# code here
        for i in range(0,N,K):
            right = min(N-1,i+K-1)
            left=i
            while left<right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1
        
            

#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends