#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
        v.sort()
        if len(v)%2==0:
            return (v[len(v)//2-1]+v[len(v)//2])//2
        return v[len(v)//2]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends