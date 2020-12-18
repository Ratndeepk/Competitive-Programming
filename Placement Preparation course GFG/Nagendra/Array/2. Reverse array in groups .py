#link https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1/?track=ppc-arrays&batchId=221#

class Solution:	
	def reverseInGroups(self, arr, N, K):
		# code here
        for i in range(0,N,K):
            if N-i-1<K:
                temp=arr[i:N]
                temp=temp[::-1]
            else:
                temp=arr[i:i+K]
                temp=temp[::-1]
            t=0
            for n in range(i,min(i+K,N)):
                arr[n]=temp[t]
                t+=1

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