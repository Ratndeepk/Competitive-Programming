def rowWithMax1s(self,arr, n, m):
		
    max_count=0
    max_index=0
    for i in range(m):
        count=0
        for j in range(n):
            if arr[i][j]==1:
                count+=1
            else:
                break
        if count>max_count:
            max_count=count
            max_index=i
    return max_index
