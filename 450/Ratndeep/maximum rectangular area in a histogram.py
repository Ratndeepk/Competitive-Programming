for _ in range(int(input())):
    n = int(input())
    hist = list(map(int,input().split()))
    max_value=0
    stack=[hist[0]]
    while len(stack)!=len(hist):
        cur_max=stack[-1]
        count=1
        temp_stack=[cur_max]
        print(stack)
        while stack and stack[-1]>=cur_max:
            temp_stack.insert(0,stack.pop())
            count+=1
            stack.pop()
            
        stack.extend(temp_stack)
        max_value=max(max_value,count*cur_max)
    print(max_value)
