class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ""
        return self.lcp(strs,0,len(strs)-1)
    
    def lcp(self,strs,l,r):
        if l==r:
            return strs[l]
        else:
            mid=(l+r)//2
            ll=self.lcp(strs,l,mid)
            lr=self.lcp(strs,mid+1,r)
            return self.cp(ll,lr)
        
    def cp(self,ll,lr):
        m =min(len(ll),len(lr))
        for i in range(m):
            if ll[i]!=lr[i]:
                return ll[:i]
        return ll[:m]


#https://leetcode.com/problems/longest-common-prefix/submissions/
