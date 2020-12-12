#User function Template for python3
class Solution:
    def smallestNumber (ob,S,D):
        # code here 
        no =''
        rem=S
        temp=D-1
        for i in range(D):
            if rem-9>0:
                no = '9'+no
                rem-=9
                temp -=1
            elif i<D-1:
                no = str(abs(rem-1))+no
                rem -= (rem-1)
                temp-=1
            else:
                no = str(rem)+no
        if no=='' or sum(list(map(int, list(no))))!=S:
            return -1
        return int(no)
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends