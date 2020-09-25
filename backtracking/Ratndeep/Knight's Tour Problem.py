def safe(x,y,a):
    if x>=0 and y>=0 and x<8 and y<8 and a[x][y]==-1:
        return True
    return False

def knight_tour(a,x,y,mov_x,mov_y,pos):
    if pos==64:
        return True


    for i in range(8):
        x_=x+mov_x[i]
        y_=y+mov_y[i]
        if safe(x_,y_,a):
            a[x_][y_]=pos
            if knight_tour(a,x_,y_,mov_x,mov_y,pos+1):
                return True
            
            a[x_][y_]=-1
            
            
    return False
    



a = [[-1 for i in range(8)]for i in range(8)]
cx = [2, 1, -1, -2, -2, -1, 1, 2] 
cy = [1, 2, 2, 1, -1, -2, -2, -1] 
pos=1
a[0][0]=0
if knight_tour(a,0,0,cx,cy,pos):
    for i in a:
        print(*i)

else:
    print("Not possible")
    

