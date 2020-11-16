# Heap

A binary heap is a binary tree where the smallest value is always at the top.

A binary heap is a binary tree where the nodes are organized to so that the smallest value is always at the top.
A min-heap has the smallest value at the top. A max-heap has the largest value at the top. We'll describe min-heaps
here, but the implementation for max-heaps is nearly identical.

## Strengths:
Quickly access the smallest item. Binary heaps allow you to grab the smallest item (the root) in O(1)O(1) time, 
while keeping other operations relatively cheap (O(lg(n))O(lg(n)) time).

Space efficient. Binary heaps are usually implemented with arrays, saving the overhead cost of storing pointers to child nodes.

## Weaknesses
Limited interface. Binary heaps only provide easy access to the smallest item. Finding other items in the heap 
takes O(n)O(n) time, since we have to iterate through all the nodes.
Uses
Priority queues are often implemented using heaps. Items are enqueued by adding them to the heap, and the 
highest-priority item can quickly be grabbed from the top.
One way to efficiently sort an array of items is to make a heap out of them and then remove items one at a 
time—in sorted order.

## Implementation
Heaps are implemented as complete binary trees.

In a complete binary tree:

Each level is filled up before another level is added, and
the bottom tier is filled in from left to right.
As we'll see, this allows us to efficiently store our heap as an array.

In a heap, every node is smaller than its children.

# Top Questions 

* Introduction to Priority Queues using Binary Heaps
* Min Heap and Max Heap Implementation in C++
* Heap Sort (Out-of-place and In-place implementation)
* Check if given array represents min heap or not
* Convert Max Heap to Min Heap in linear time
* Find K’th largest element in an array
* Sort K-Sorted Array
* Merge M sorted lists of variable length
* Find K’th smallest element in an array
* Find smallest range with at-least one element from each of the given lists
* Merge M sorted lists each containing N elements
* External merge sort
* Huffman Coding
* Find first k maximum occurring words in given set of strings
* Find first k non-repeating characters in a string in single traversal