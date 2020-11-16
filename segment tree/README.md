# Segment Tree 

A Segment Tree is a data structure that allows answering range queries over an array effectively, 
while still being flexible enough to allow modifying the array. This includes finding the sum of 
consecutive array elements a[l…r], or finding the minimum element in a such a range in O(logn) time. 
Between answering such queries the Segment Tree allows modifying the array by replacing one element, 
or even change the elements of a whole subsegment (e.g. assigning all elements a[l…r] to any value, 
or adding a value to all element in the subsegment).

In general a Segment Tree is a very flexible data structure, and a huge number of problems can be solved 
with it. Additionally it is also possible to apply more complex operations and answer more complex queries 
(see Advanced versions of Segment Trees). In particular the Segment Tree can be easily generalized to 
larger dimensions. For instance with a two-dimensional Segment Tree you can answer sum or minimum queries 
over some subrectangle of a given matrix. However only in O(log2n) time.

One important property of Segment Trees is, that they require only a linear amount of memory. 
The standard Segment Tree requires 4n vertices for working on an array of size n.

# Top Segment Tree Questions 

* SPOJ - KQUERY [Persistent segment tree / Merge sort tree]
* Codeforces - Xenia and Bit Operations
* UVA 11402 - Ahoy, Pirates!
* SPOJ - GSS3
* Codeforces - Distinct Characters Queries
* Codeforces - Knight Tournament [For beginners]
* Codeforces - Ant colony
* Codeforces - Drazil and Park
* Codeforces - Circular RMQ
* Codeforces - Lucky Array
* Codeforces - The Child and Sequence
* Codeforces - DZY Loves Fibonacci Numbers [Lazy propagation]
* Codeforces - Alphabet Permutations
* Codeforces - Eyes Closed
* Codeforces - Kefa and Watch
* Codeforces - A Simple Task
* Codeforces - SUM and REPLACE
* COCI - Deda [Last element smaller or equal to x / Binary search]
* Codeforces - The Untended Antiquity [2D]
* CSES - Hotel Queries
* CSES - Polynomial Queries
* CSES - Range Updates and Sums

Source: CP-algorithms 