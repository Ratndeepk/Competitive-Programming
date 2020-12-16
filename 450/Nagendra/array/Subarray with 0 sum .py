#https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1

#Complete this function
def subArrayExists(arr,n):
    ##Your code here
    #Return true or false
    sum=0
    store =set()
    for i in range(n):
        sum+=arr[i]
        if sum==0 or sum in store:
            return 1
        store.add(sum)
    return 0
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends