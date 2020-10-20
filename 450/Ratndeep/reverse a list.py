def reverse(start,end,my_list):
    if start>=end:
        return
    my_list[start],my_list[end]=my_list[end],my_list[start]
    reverse(start+1,end-1,my_list)

my_list = list(map(int,input().split()))
reverse(0,len(my_list)-1,my_list)
print(my_list)
