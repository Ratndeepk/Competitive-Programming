def printLargest(arr):
    my_number = str(arr[0])
	    
    for i in range(1,len(arr)):
        if int(my_number+str(arr[i]))>=int(str(arr[i])+my_number):
            my_number+=str(arr[i])
        else:
            my_number = str(arr[i])+my_number
    return my_number
print(printLargest([3,30,34,5,9]))
