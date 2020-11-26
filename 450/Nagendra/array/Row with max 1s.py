#User https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#
class Solution:

	def rowWithMax1s(self, arr, n, m):
	# code here
	col = m
	ind = n
	for i in range(n):
	    for j in arr[i]:
	        if j == 1:
	        if arr[i].index(1) < col:
	        col = arr[i].index(1)
	        ind = i
	        if col == 0:
	            return i
        if ind == n:
            return -1
	return ind


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]

        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
