n = int(input())
my_list = list(map(int,input().split()))

low=0
mid=0
high=n-1

while mid<=high:
    if my_list[mid]==0:
        my_list[low],my_list[mid]=my_list[mid],my_list[low]
        mid+=1
        low+=1
    elif my_list[mid]==2:
        my_list[high],my_list[mid]=my_list[mid],my_list[high]
        high-=1
    else:
        mid+=1

print(my_list)
