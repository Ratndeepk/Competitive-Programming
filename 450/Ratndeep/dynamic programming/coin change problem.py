for _ in range(int(input())):
    n,m = map(int,input().split()) # n -> destination money 
    coins = list(map(int,input().split())) # coins available  

    """
    Coins  | 0  | 1  | 2  | 3  | 4  | 5  |
    []     | 1  | 0  | 0  | 0  | 0  | 0  |
    [1]    | 1  | 1  | 1  | 1  | 1  | 1  |
    [1,2]  | 1  | 1  | 2  | 2  | 3  | 3  |
    [1,2,5]| 1  | 1  | 2  | 2  | 3  | 4  |
    

    Considering coins go n-coin taken on left 
    Not Considering coin just go row-1 

    """

    coin_matrix = [[0 for x in range(n+1)] for x in range(m+1)] 
     

    for i in range(m+1):
        coin_matrix[i][0]=1 
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if j-coins[i-1]>=0:
                coin_matrix[i][j]=coin_matrix[i-1][j] + coin_matrix[i][j-coins[i-1]] 
            else:
                coin_matrix[i][j]=coin_matrix[i-1][j] 

    for i in coin_matrix:
        print(*i)
    print(coin_matrix[m][n])  
