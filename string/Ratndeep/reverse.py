for _ in range(int(input())):
    n = input().split('.')
    for i in range(len(n)-1,-1,-1):
        if i!=0:
            print(n[i],end=".")
        else:
            print(n[i])
  
