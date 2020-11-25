class Solution:
    def countAndSay(self, n: int) -> str:
        if n==2:
            return "11"
        if n==1:
            return "1" 
        base = self.countAndSay(n-1)
    
        
        check=[] 
        new_base=""
        index=0
        i=0
        while i<len(base)-1:
            
            count=1
            while i+1<len(base) and base[i+1]==base[i]:
                count+=1 
                i+=1 
            new_base+=str(count)+base[i] 
            i+=1
        if i==len(base)-1:
            new_base+="1"+base[i]
        return new_base

sol=Solution()
print(sol.countAndSay(int(input())))