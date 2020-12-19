#User function Template for python3
def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    # code here
    ratio=[]
    for i in Items:
        ratio.append([i.value/i.weight,i.value,i.weight])
    ratio.sort(reverse=True)
    maxx=0
    for i in ratio:
        
        if W>0 and i[2]<=W:
            W-=i[2]
            maxx+=i[1]
        elif W>0:
            maxx+=i[0]*W
            W=0
    return maxx
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]

        print("%.2f" %fractionalknapsack(W,Items,n))

# } Driver Code Ends