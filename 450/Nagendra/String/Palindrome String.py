#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
		# code here
	    if S == S[::-1]:
	        return 1
        else:
            return 0


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T = int(input())
	for i in range(T):
	S = input()
	ob = Solution()
	answer = ob.isPlaindrome(S)
	print(answer)

# } Driver Code Ends
