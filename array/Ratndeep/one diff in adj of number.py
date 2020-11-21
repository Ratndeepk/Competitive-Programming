n = int(input())
if n<=10:
    for i in range(1,n):
        print(i,end=" ")
    print()
else:
    for i in range(1,11):
        print(i,end=" ")
    for i in range(11,n):
        cur_num = str(i)
        x=0
        flag=0
        while x<len(cur_num)-1:
            if abs(int(cur_num[x])-int(cur_num[x+1]))!=1:
                flag=1
                break
            x+=1
        if flag==0:
            print(i,end=" ")
    print()
