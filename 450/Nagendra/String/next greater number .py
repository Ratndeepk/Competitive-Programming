#link  https://practice.geeksforgeeks.org/problems/next-permutation/0


def next_perm(n, arr):

    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            if i == n-2:
                # print('one')
                return arr[::-1]
        else:
            break
    for i in range(n-1):
        if arr[i] <= arr[i+1]:
            if i == n-2:
                if arr[i] == arr[i+1]:
                    k = i
                    while k > 0:
                        if arr[k] != arr[k-1]:
                            arr[k], arr[k-1] = arr[k-1], arr[k]
                            # print("two")
                            return arr
                else:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    # print("th")
                    return arr
        else:
            break
    i = n-1

    while i > 0:
        if arr[i-1] < arr[i]:
            break
        i -= 1
    minn = arr[i-1]
    temp = i
    small = float('inf')
    while temp < n:
        if arr[temp] > minn:
            if arr[temp] < small:
                small = arr[temp]
                ind = temp
        temp += 1
    arr[ind], arr[i-1] = arr[i-1], arr[ind]
    a = arr[:i]
    b = arr[i:]
    b.sort()
    for i in b:
        a.append(i)
    # print("fff")
    return a


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    print(*next_perm(n, arr))
