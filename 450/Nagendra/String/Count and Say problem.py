#link https://leetcode.com/problems/count-and-say/solution/
class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for i in range(n-1):
            n = ''
            c = 1
            j = 0
            while j < len(s):
                if j < len(s)-1 and s[j] == s[j+1]:
                    c += 1
                    j += 1
                    continue

                if c > 1:
                    n += str(c)+s[j]
                    c = 1
                else:
                    n += str(c)+s[j]
                    c = 1

                j += 1

            s = n
        return s
