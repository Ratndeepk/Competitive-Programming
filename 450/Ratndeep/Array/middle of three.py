
class Solution:
    def middle(self,A,B,C):
        #code here
        if A<B:
            return B if B<C else max(A,C)
        return A if A<C else max(B,C)


s = Solution()
a,b,c = map(int,input().split())
print(s.middle(a,b,c))