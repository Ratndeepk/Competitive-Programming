"""
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.
"""

#https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#


class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		count=0
		max_count=-1
	    cur_index=m
	    final_sol=-1
		for i in range(n):
		   
		    for j in range(cur_index-1,-1,-1):
		        if arr[i][j]==1:
		            cur_index=j 
		            final_sol=i
		        else:
		            break 
		        
	    return final_sol
