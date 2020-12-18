#https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1/?category[]=sliding-window&page=1&query=category[]sliding-windowpage1#
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        max=0
        upto=0
        c=0
        start=0
        for i in range(N):
            if c==K:
                upto-=Arr[start]
                start+=1
                c-=1
            if upto+Arr[i] >upto:
                upto+=Arr[i]
                c+=1
            if upto>max and c==K:
                max=upto
        return max
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends