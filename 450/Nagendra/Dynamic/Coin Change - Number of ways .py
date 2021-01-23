#{ 
#Driver Code Starts
#Initial Template for Python 3




 # } Driver Code Ends

#User function Template for python3

##Complete this function
# def coun(coins,numberOfCoins,value):
#     if value==0:
#         return 1
#     if value<=0:
#         return 0
    
#     if numberOfCoins<=0:
#         return 0
    
    
#     # if coins[numberOfCoins-1]<=value:
#     return (coun(coins, numberOfCoins, value-coins[numberOfCoins-1]) + coun(coins, numberOfCoins-1, value))
        
#     # else:
#     #     return coun(coins, numberOfCoins-1,value)
        
def numberOfWays(coins,numberOfCoins,value):
    
    # return coun(coins,numberOfCoins,value)
    
    
    mat = [[0 for i in range(value+1)] for j in range(numberOfCoins+1)]
    
    for no in range(numberOfCoins+1):
        for val in range(value+1):
            if val==0:
                mat[no][val]=1
            elif no==0:
                mat[no][val]=0
            elif coins[no-1]<=val:
                mat[no][val] = mat[no][val - coins[no-1]]+ mat[no-1][val]
            else:
                mat[no][val] = mat[no-1][val]
            # else:
                # mat[no][val] = mat[no][val-1]
            
    # print(mat)
    return mat[numberOfCoins][value]
            
    
      
#{ 
#Driver Code Starts.

def main():
    testcases=int(input())
    while(testcases>0):
        value=int(input())
        numberOfCoins=int(input())
        coins=[int(x) for x in input().strip().split()]
        print(numberOfWays(coins,numberOfCoins,value))
        testcases-=1

if __name__=="__main__":
    main()
    
#} Driver Code Ends
