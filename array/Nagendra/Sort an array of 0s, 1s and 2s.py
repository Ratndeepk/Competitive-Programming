#link https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1


def sort012(arr, n):
    # code here

   low = 0
   mid = 0
   high = n-1
   temp = 0

   while mid <= high:
       if arr[mid] == 0:

           arr[low], arr[mid] = arr[mid], arr[low]

           low += 1
           mid += 1
        elif arr[mid] == 2:

            arr[high], arr[mid] = arr[mid], arr[high]

            high -= 1
        else:
            mid += 1


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
