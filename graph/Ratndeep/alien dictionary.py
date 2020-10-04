from collections import defaultdict
'''
dict : array of strings denoting the words in alien langauge
N : Size of the dictionary
K : Number of characters
'''
string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
final_string=""
def topsortutil(stack,graph,cur_str,visited):
    visited[ord(cur_str)-97]=True
    for i in graph[cur_str]:
        if visited[ord(i)-97]==False:
            topsortutil(stack,graph,i,visited)
    stack.insert(0,cur_str)



def toposort(graph,v):
    # Code here
    stack=[]
    visited= [False]*v
    for i in range(v):
        if visited[ord(string[i])-97]==False:
            topsortutil(stack,graph,string[i],visited)
    return "".join(stack)

    
def findOrder(dict, N, K):
    # code here
    # return the string containing all k characters in correct order
    graph=defaultdict(list)
    index=0
    while index<n-1:
        str1 = dict[index]
        str2 = dict[index+1]
        for i in range(len(min(str1,str2))):
            if str1[i]!=str2[i]:
                graph[str1[i]].append(str2[i])
                break
        index+=1
    return toposort(graph,k)
