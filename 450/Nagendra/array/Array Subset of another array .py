#code https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0

for _ in range(int(input())):
    m, n = map(int, input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int, input().split()))
    l=set()
    flag='Yes'
    
    for i in arr1:
        l.add(i)
    for i in arr2:
        if i not in l:
            flag='No'
            break
    print(flag)
            

    