ans={}
class Solution:
    
    def climbStairs(self, n: int) -> int:
        global ans
        if n in ans:
            return ans[n]
        if n==0:
            ans[n]=1
            return 1
        if n==1:
             
            ans[n]=1
            return 1
        else:
            result = self.climbStairs(n-1)+self.climbStairs(n-2)
            ans[n]=result 
            return result

s =Solution()
s.climbStairs(int(input()))