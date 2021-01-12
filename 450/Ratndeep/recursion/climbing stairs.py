"""
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
print(s.climbStairs(int(input())))

"""
def no_of_ways(n,m):
    if n==0:
        return 1
    if n==1:
        return 1
    i=1
    count=0
    while i<=m and i<=n:
        count+=no_of_ways(n-i,m)
        i+=1
    return count
n = int(input())
m = int(input())
print(no_of_ways(n,m))