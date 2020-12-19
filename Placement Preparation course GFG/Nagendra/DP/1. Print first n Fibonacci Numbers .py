#User function Template for python3

def printFibb(n):
    # your code here
    arr = [0]*n
    arr[0]=1
    
    if n<=1:
        return arr
    arr[1]=1
    
    for i in range(2,n):
        arr[i] = arr[i-1]+arr[i-2]
    return arr



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = printFibb(n)
        for i in range (len (res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends