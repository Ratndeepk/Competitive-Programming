class Node:
    
    def __init__(self,data):
        self.vertex=data
        self.next=None

class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = [None] * self.v
    
    def add_edge(self,src,des):
        node = Node(des)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[des]
        self.graph[des] = node

    def traverse(self):
        
        for i in range(self.v):
            temp=self.graph[i]
            print(i,end='')
            while(temp != None):
                print(" -> {}".format(temp.vertex), end='')
                temp=temp.next
            print("\n")

v=5
graph = Graph(v)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.traverse()
