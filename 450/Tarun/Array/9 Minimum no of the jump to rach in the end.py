# 9 Minimum no of the jump to rach in the end
n = 6
arr = [1, 4, 3, 2, 6, 7]
dp = [float('inf') for i in range(n)]
dp[0] = 0
for i in range(n):
    for j in range(i+1,i + arr[i]+1):
        if j < n:
            dp[j] = min(dp[j],dp[i] + 1)
            pre = j
        else:
            break
print(dp[-1] if dp[-1] != float('inf') else -1)