
-----------------

2.2.1 Give a trace, in the style of the trace given at the beginning of this section, show-
ing how the keys A E Q S U Y E I N O S T are merged with the abstract in-place
merge() method.
2.2.2 Give traces, in the style of the trace given with Algorithm 2.4, showing how the
keys E A S Y Q U E S T I O N are sorted with top-down mergesort.
2.2.3 Answer Exercise 2.2.2 for bottom-up mergesort.
2.2.4 Does the abstract in-place merge produce proper output if and only if the two
input subarrays are in sorted order? Prove your answer, or provide a counterexample.
2.2.5 Give the sequence of subarray sizes in the merges performed by both the top-
down and the bottom-up mergesort algorithms, for N = 39.
2.2.6 Write a program to compute the exact value of the number of array accesses used
by top-down mergesort and by bottom-up mergesort. Use your program to plot the val-
ues for N from 1 to 512, and to compare the exact values with the upper bound 6N lg N.
2.2.7 Show that the number of compares used by mergesort is monotonically increas-
ing (C(N+1) > C(N) for all N > 0).
2.2.8 Suppose that Algorithm 2.4 is modified to skip the call on merge() whenever
a[mid+1]. Prove that the number of compares used to mergesort a sorted
a[mid] <= array is linear.
2.2.9 Use of a static array like aux[] is inadvisable in library software because multiple
clients might use the class concurrently. Give an implementation of Merge that does not
use a static array. Do not make aux[] local to merge() (see the Q&A for this section).
Hint : Pass the auxiliary array as an argument to the recursive sort().

2.2.10 Faster merge. Implement a version of merge() that copies the second half of
a[] to aux[] in decreasing order and then does the merge back to a[]. This change al-
lows you to remove the code to test that each of the halves has been exhausted from the
inner loop. Note: The resulting sort is not stable (see page 341).
2.2.11 Improvements. Implement the three improvements to mergesort that are de-
scribed in the text on page 275: Add a cutoff for small subarrays, test whether the array is
already in order, and avoid the copy by switching arguments in the recursive code.
2.2.12 Sublinear extra space. Develop a merge implementation that reduces the extra
space requirement to max(M, N/M), based on the following idea: Divide the array into
N/M blocks of size M (for simplicity in this description, assume that N is a multiple
of M). Then, (i) considering the blocks as items with their first key as the sort key, sort
them using selection sort; and (ii) run through the array merging the first block with
the second, then the second block with the third, and so forth.
2.2.13 Lower bound for average case. Prove that the expected number of compares used
by any compare-based sorting algorithm must be at least ~N lg N (assuming that all
possible orderings of the input are equally likely). Hint: The expected number of com-
pares is at least the external path length of the compare tree (the sum of the lengths of
the paths from the root to all leaves), which is minimized when it is balanced.
2.2.14 Merging sorted queues. Develop a static method that takes two queues of sorted
items as arguments and returns a queue that results from merging the queues into
sorted order.
2.2.15 Bottom-up queue mergesort. Develop a bottom-up mergesort implementation
based on the following approach: Given N items, create N queues, each containing one
of the items. Create a queue of the N queues. Then repeatedly apply the merging opera-
tion of Exercise 2.2.14 to the first two queues and reinsert the merged queue at the end.
Repeat until the queue of queues contains only one queue.
2.2.16 Natural mergesort. Write a version of bottom-up mergesort that takes advan-
tage of order in the array by proceeding as follows each time it needs to find two arrays
to merge: find a sorted subarray (by incrementing a pointer until finding an entry that
is smaller than its predecessor in the array), then find the next, then merge them. Ana-
lyze the running time of this algorithm in terms of the array size and the number of

2.2.17 Linked-list sort. Implement a natural mergesort for linked lists. (This is the
method of choice for sorting linked lists because it uses no extra space and is guaranteed
to be linearithmic.)
2.2.18 Shuffling a linked list. Develop and implement a divide-and-conquer algo-
rithm that randomly shuffles a linked list in linearithmic time and logarithmic extra
space.
2.2.19 Inversions. Develop and implement a linearithmic algorithm for computing
the number of inversions in a given array (the number of exchanges that would be
performed by insertion sort for that array—see Section 2.1). This quantity is related
to the Kendall tau distance; see Section 2.5.
2.2.20 Indirect sort. Develop and implement a version of mergesort that does not re-
arrange the array, but returns an int[] array perm such that perm[i] is the index of the
i th smallest entry in the array.
2.2.21 Triplicates. Given three lists of N names each, devise a linearithmic algorithm
to determine if there is any name common to all three lists, and if so, return the first
such name.
2.2.22 3-way mergesort. Suppose instead of dividing in half at each step, you divide
into thirds, sort each third, and combine using a 3-way m

2.2.23 Improvements. Run empirical studies to evaluate the effectiveness of each of the
three improvements to mergesort that are described in the text (see Exercise 2.2.11).
Also, compare the performance of the merge implementation given in the text with the
merge described in Exercise 2.2.10. In particular, empirically determine the best value
of the parameter that decides when to switch to insertion sort for small subarrays.
2.2.24 Sort-test improvement. Run empirical studies for large randomly ordered ar-
rays to study the effectiveness of the modification described in Exercise 2.2.8 for ran-
dom data. In particular, develop a hypothesis about the average number of times the
test (whether an array is sorted) succeeds, as a function of N (the original array size for
the sort).
2.2.25 Multiway mergesort. Develop a mergesort implementation based on the idea of
doing k-way merges (rather than 2-way merges). Analyze your algorithm, develop a hy-
pothesis regarding the best value of k, and run experiments to validate your hypothesis.
2.2.26 Array creation. Use SortCompare to get a rough idea of the effect on perfor-
mance on your machine of creating aux[] in merge() rather than in sort().
2.2.27 Subarray lengths. Run mergesort for large random arrays, and make an empiri-
cal determination of the average length of the other subarray when the first subarray
exhausts, as a function of N (the sum of the two subarray sizes for a given merge).
2.2.28 Top-down versus bottom-up. Use SortCompare to compare top-down and bot-
tom-up mergesort for N=103, 104, 105, and 106
.
2.2.29 Natural mergesort. Determine empirically the number of passes needed in a
natural mergesort (see Exercise 2.2.16) for random Long keys with N=103, 106, and
109
. Hint: You do not need to