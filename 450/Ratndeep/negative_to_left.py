my_list = list(map(int,input().split()))

low=0
high=len(my_list)-1

while low<high:
    if my_list[low]<0 and my_list[high]<0:
        low+=1
    elif my_list[high]>0 and my_list[low]>0:
        high-=1

    elif my_list[low]>0 and my_list[high]<0:
        my_list[low],my_list[high]=my_list[high],my_list[low]
        low+=1
        high-=1
    else:
        low+=1
        high-=1
print(my_list)
