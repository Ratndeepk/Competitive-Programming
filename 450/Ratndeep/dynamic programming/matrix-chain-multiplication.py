"""
Matrix Chain Multiplication

Lets  take A1, A2, A3, A4 

((A1.A2).A3).A4)   OR  (A1.A2).(A3.A4) 

T(n) = 2nCn/(n+1) 

Abdul Bari (Matrix Chain Multiplication)
https://www.youtube.com/watch?v=prx1psByp7U&t=2s&ab_channel=AbdulBari

Time Complexity - O(n^2)
Example - 

A1 (5X4)  A2 (4X6)  A3 (6X2) A4 (2X7) 

Table M
 | 1 | 2   | 3  | 4  |
1| 0 | 120 | 88 |158 |
2|   | 0   | 48 |104 |
3|   |     | 0  | 84 |
4|   |     |    | 0  | 

Table S
 | 1 | 2   | 3  | 4  |
1|   | 1   | 1  | 3  |
2|   |     | 2  | 3  |
3|   |     |    | 3  |
4|   |     |    |    | 

"""
def MatrixChainOrder(p, n): 
	m = [[0 for x in range(n)] for x in range(n)] 


	for i in range(1, n): 
		m[i][i] = 0
 
	for L in range(2, n): 
		for i in range(1, n-L + 1): 
			j = i + L-1
			m[i][j] = float("inf")
			for k in range(i, j): 

			
				q = m[i][k] + m[k + 1][j] + p[i-1]*p[k]*p[j] 
				if q < m[i][j]: 
					m[i][j] = q 

	return m[1][n-1] 

arr = [1, 2, 3, 4] 
size = len(arr) 

print(str(MatrixChainOrder(arr, size))) 


