
def find_combinations(n,r):
    if r>n:
        return 0
    combinations = [0 for i in range(n+1)]
    combinations[0]=1 
    for i in range(1,n+1):
        combinations[i] = i*combinations[i-1]  # for n=5 combinations = [1,1,2,6,24,120]
                

    return (combinations[n]//(combinations[r]*combinations[n-r]))%1000000007  
    # n=5 r=3  combinations[n]=120 combinations[r]=6 combinations[n-r]=2


n,r = map(int,input().split())
print(find_combinations(n,r))