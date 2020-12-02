#link https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1#


class Solution:
    def findTwoElement(self, arr, n):
        # code here

        lis = []
        for i in range(n):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                lis.append(abs(arr[i]))
        for i in range(n):
            if arr[i] > 0:
                lis.append(i+1)
                break
        return lis


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc = tc-1
# } Driver Code Ends
