class Solution:
    def findComplement(self, num: int) -> int:
        ans=0
        mul=1
        if num==0:
            return 1
        while num:
            ans += mul*(1-num&1)
            num>>=1
            mul*=2
        return ans

#https://leetcode.com/problems/number-complement/submissions/
