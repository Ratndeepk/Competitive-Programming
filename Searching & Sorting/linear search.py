element = int(input())

my_list = list(map(int,input().split()))
flag=0
for i in range(len(my_list)):
    if my_list[i]==element:
        flag=1
        break
if flag==1:
    print("Found at index:",i)
else:
    print("Element not found")
