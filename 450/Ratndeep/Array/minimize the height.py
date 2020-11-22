"""
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.
"""



class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        if n==1:
            return 0
        arr.sort()
        answer=arr[-1]-arr[0]
        smallest = arr[0]+k
        largest = arr[-1]-k
        
        if smallest>largest:
            smallest,largest=largest,smallest
        
        for i in range(1,n-1):
            add=arr[i]+k
            sub=arr[i]-k
            if add<=largest or sub>=smallest:
                continue
            if add-smallest<largest-sub:
                largest=add
            else:
                smallest=sub

        return min(answer,largest-smallest)