# Graph 

A graph is a common data structure that consists of a finite set of nodes (or vertices) and a set of edges connecting them.
A pair (x,y) is referred to as an edge, which communicates that the x vertex connects to the y vertex.

## Types of graphs:

### Undirected Graph:
In an undirected graph, nodes are connected by edges that are all bidirectional. For example 
if an edge connects node 1 and 2, we can traverse from node 1 to node 2, and from node 2 to 1.

### Directed Graph
In a directed graph, nodes are connected by directed edges – they only go in one direction. 
For example, if an edge connects node 1 and 2, but the arrow head points towards 2, we can only 
traverse from node 1 to node 2 – not in the opposite direction.

## Types of Graph Representations:

### Adjacency List
To create an Adjacency list, an array of lists is used. The size of the array is equal to the number of nodes.
A single index, array[i] represents the list of nodes adjacent to the ith node.

### Adjacency Matrix:
An Adjacency Matrix is a 2D array of size V x V where V is the number of nodes in a graph. 
A slot matrix[i][j] = 1 indicates that there is an edge from node i to node j.

Source: Educative.io 

# Top Graph Questions 

* Terminology and Representations of Graphs
* Graph Implementation in C++ using STL
* Graph Implementation in C++ (without using STL)
* Implement Graph Data Structure in C
* Graph Implementation in Java using Collections
* Breadth First Search (BFS) | Iterative & Recursive Implementation
* Depth First Search (DFS) | Iterative & Recursive Implementation
* Arrival and Departure Time of Vertices in DFS
* Types of edges involved in DFS and relation between them
* Bipartite Graph
* Determine if a graph is Bipartite Graph using DFS
* Minimum number of throws required to win Snake and Ladder game
* Topological Sort Algorithm for DAG using DFS
* Kahn’s Topological Sort Algorithm
* Transitive Closure of a Graph
* Check if an undirected graph contains cycle or not
* Total number of paths in given digraph from given source to destination having exactly m edges
* Determine if an undirected graph is a Tree (Acyclic Connected Graph)
* 2-Edge Connectivity in a Graph
* 2-Vertex Connectivity in the graph
* Check if given digraph is a DAG (Directed Acyclic Graph) or not
* Disjoint-Set Data Structure (Union Find Algorithm)
* Chess Knight Problem | Find Shortest path from source to destination
* Check if given Graph is Strongly Connected or not
* Check if Graph is Strongly Connected or not using one DFS Traversal
* Union-Find Algorithm for Cycle Detection in a graph
* Kruskal’s Algorithm for finding Minimum Spanning Tree
* Single-Source Shortest Paths — Dijkstra’s Algorithm
* Single-Source Shortest Paths — Bellman Ford Algorithm
* All-Pairs Shortest Paths — Floyd Warshall Algorithm
* Find Cost of Shortest Path in DAG using one pass of Bellman-Ford
* Least Cost Path in Weighted Digraph using BFS
* Find maximum cost path in graph from given source to destination
* Determine negative-weight cycle in a graph
* Print all k-colorable configurations of the graph (Vertex coloring of graph)
* Print all Hamiltonian path present in a graph
* Greedy coloring of graph