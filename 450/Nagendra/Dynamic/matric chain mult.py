def matrix_chain(p):
    length = len(p)
    m=[[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        m[i][i]=0
    print(m)
    for l in range(2,length):
        for i in range(1,length-l+1):
            j=i+l-1
            m[i][j]=float('inf')
            for k in range(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if q<m[i][j]:
                    m[i][j]=q
    print(m)
    return m[1][length-1]

p=[1,2,1,4,1]
print(matrix_chain(p))