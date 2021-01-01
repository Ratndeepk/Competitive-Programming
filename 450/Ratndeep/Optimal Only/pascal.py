def pascal(n):
    for i in range(n):
        c=1
        print(c,end=" ")
        for j in range(1,i):
            c*=(i-j+1)//j
            print(c,end=" ") 
        print() 
    
n = int(input())
pascal(n)