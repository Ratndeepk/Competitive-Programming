
def find_combinations(n,r):
    if r>n:
        return 0
    combinations = [0 for i in range(n+1)]
    combinations[0]=1 
    for i in range(1,n+1):
        combinations[i] = i*combinations[i-1]
                
    return (combinations[n]//(combinations[r]*combinations[n-r]))%1000000007


n,r = map(int,input().split())
print(find_combinations(n,r))