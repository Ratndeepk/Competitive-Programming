#https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1#

def valueEqualToIndex(self,arr, n):
		# code here
	index=[]
	for i in range(n):
		if arr[i]==i+1:
		    index.append(i+1) 
	return index