''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT
import math 
import __pypy__

def main():
	n = int(input())
	numbers = list(map(int,input().split()))


	matrix = [[0 for i in range(n)] for i in range(n)]


	for i in range(n):
		for j in range(n):
			if i!=j:
				matrix[i][j]=numbers[i]*numbers[j]


	sol = float("-inf")
	for i in range(n-1):
		index=i
		cur_sol=0
		for j in range(n-1,-1,-1):
			cur_sol+=matrix[index][j]
			index+=1 
			if index>=n:
				break
		if sol<cur_sol//2:
			sol=cur_sol//2
	
	flag=2 
	while(n-flag):
		index=0 
		cur_sol=0 
		for j in range(n-flag,-1,-1):
			cur_sol+=matrix[index][j] 
			index+=1 
			if index>=n:
				break 
		if sol<cur_sol//2:
			sol=cur_sol//2 

		flag+=1 
	#index=0
	cur_sol=[] 
	#for i in range(n-1,-1,-1):
	#	cur_sol.append(matrix[index][i])
	#	index+=1 
	for i in matrix:
		cur_sol.extend(i) 

		
	if sol<max(cur_sol):
		sol=max(cur_sol) 
	if n==1:
		print(0)
	else:
		print(sol)
	
	
main()
