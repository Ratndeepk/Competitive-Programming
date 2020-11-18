import math
def countSquares(N):
        
    ans = int(math.sqrt(N-1))
        
    return ans

print(countSquares(int(input())))