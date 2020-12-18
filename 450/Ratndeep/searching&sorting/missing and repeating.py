
class Solution:
    def findTwoElement( self,arr, n): 
        
        d={}
        for i in range(1,n+1):
            d[i]=0
        for i in range(n):
            d[arr[i]]=d.get(arr[i],0)+1
            if d[arr[i]]>1:
                key=arr[i]
        for j in range(1,n+1):
            if d[j]==0:
                break
        
        return key,j
       



if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
