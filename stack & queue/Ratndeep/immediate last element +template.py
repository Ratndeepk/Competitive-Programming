def top(s):
    if s!=[]:
        return s[len(s)-1]
    else:
        return -1
class Stack:
    def __init__(self):
        self.s = []
    def push(self,x):
        self.s.append(x)
        
    def pop_(self):
        if self.s==[]:
            return -1
        popped=self.s.pop()
        if top(self.s)<popped:
            return top(self.s)
        else:
            return -1
   

if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        sa=Stack()
        for i in range(n-1,-1,-1):
            sa.push(a[i])
     
        while sa.s!=[]:
            print(sa.pop_(), end=" ")
        
        print()
