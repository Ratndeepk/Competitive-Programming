class Solution:
    def median(self, matrix, r, c):
    	#code here 
        m=[]
        for i in matrix:
            m.extend(i)
        m.sort()
        return m[len(m)//2]
