from collections import defaultdict

def getVerticalOrder(root, hd, m): 
    if root is None: 
        return

    try: 
        m[hd].append(root.data) 
    except: 
        m[hd] = [root.data] 
      
 
    getVerticalOrder(root.left, hd-1, m) 
    getVerticalOrder(root.right, hd+1, m) 



def bottomView(root):
    hd=0
    m = defaultdict(list)
    getVerticalOrder(root, hd, m)
    final_list = []
    for i,j in m.items():
        print(i,j)
        final_list.append(j[-1])
    return final_list
