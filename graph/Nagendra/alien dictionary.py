#User function Template for python3

'''
dict : array of strings denoting the words in alien langauge
N : Size of the dictionary
K : Number of characters
'''

def topSort(v,stack,visited,graph):
    
    visited[v]=1
    
    for i in graph[v]:
        if visited[i]==0:
            topSort(i,stack,visited,graph)
    
    stack.insert(0,chr(v+ord('a')))
    #print(stack)#

from collections import defaultdict
def findOrder(dict, N, K):
    # code here
    # return the string containing all k characters in correct order
    graph=defaultdict(list)
    
    for i in range(N-1):
        for j in range(len(dict[i])):
            if dict[i][j]!=dict[i+1][j]:
                #print(dict[i][j],dict[i+1][j],i,j)
                graph[ord(dict[i][j])-ord('a')].append(ord(dict[i+1][j])-ord('a'))
                #print(graph)
                break
    
    stack=[]
    visited=[0]*K
    
    for v in range(k):
        if visited[v]==0:
            topSort(v,stack,visited,graph)
    
    return "".join(stack)
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        
        order = findOrder(alien_dict,n,k)
        
        x = sort_by_order(order)
        x.sort_this_list(duplicate_dict)
        
        if duplicate_dict == alien_dict:
            print(1)
        else:
            print(0)


# } Driver Code Ends