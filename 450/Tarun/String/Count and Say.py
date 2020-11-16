# Count and Say
def solve(n):
    arr = [1]
    while(n-1):
        temp = []
        d = {}
        i = 0
        while(i < len(arr)):
            val = arr[i]
            if val == arr[i]:
                cnt = 0
                while(i < len(arr) and val == arr[i]):
                    cnt += 1
                    i += 1
                temp.append(cnt)
                temp.append(val)
        arr = temp
        n -= 1
    return "".join([str(i) for i in arr])
    
n = 4
solve(n)