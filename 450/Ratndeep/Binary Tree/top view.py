def topview(root,ans,move,level):
    if root==None:
        return 
        
    if move not in ans:
        ans[move]=[root.data,level]
    elif ans[move][1]>level:
        ans[move]=[root.data,level]
    topview(root.left,ans,move-1,level+1)
    topview(root.right,ans,move+1,level+1)

def topView(root):
    
    
    ans={}
    topview(root,ans,0,0)
    for i in sorted(ans.keys()):
        print(ans[i][0],end=" ") 
    
    
from collections import deque
import queue 

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def make_tree():
    n=int(input())
    l=list(map(str,input().split()))
    head=None
    q=deque()
    i=0
    while(n>0):
        a,b,c=l[i],l[i+1],l[i+2]
        if(not head):
            head=Node(int(a))
            q.append(head)
        pick=q[0]
        q.popleft()
        if(c=='L'):
            pick.left=Node(int(b))
            q.append(pick.left)
        n=n-1
        if(not n):
            break
        a,b,c=l[i+3],l[i+4],l[i+5]
        if(c=='R'):
            pick.right=Node(int(b))
            q.append(pick.right)
        i=i+6
        n=n-1
    return head
            

if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        root=make_tree()
        topView(root)
        print()

