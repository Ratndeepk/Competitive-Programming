for _ in range(int(input())):
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    p=1
    # for k in range(x):
    #     i, j = 0,1
    #     # print(*arr)
    #     arr[i] = arr[i]^(2)
    #     arr[j] = arr[j]^(2)
        # if (k+1)%2==0:
        #     j+=1
        # else:
        #     i+=1
        # print(*arr)
    if x%2==0:
        print(*arr)
    else:
        i, j = 0,1
        arr[i] = arr[i]^(2)
        arr[j] = arr[j]^(2)
        print(*arr)
    # print(*arr)

    