#Bubble Sort Algorithm: A simple sorting method that repeatedly steps through the list, 
#compares adjacent elements, and swaps them if they are in the wrong order. 
#It has a time complexity of O(n^2) and is best used for educational purposes due to inefficiency on large datasets.

array = list(map(int,input().split()))
n = len(array)

for i in range(n):
    swapped = False
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
            swapped = True

    if swapped == False:
        break


print(array)
