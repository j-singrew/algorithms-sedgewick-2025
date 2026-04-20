2.1.23 Deck sort. Ask a few friends to sort a deck of cards (see Exercise 2.1.13). Ob-
serve them carefully and write down the method(s) that they use.
2.1.24 Insertion sort with sentinel. Develop an implementation of insertion sort that
eliminates the j>0 test in the inner loop by first putting the smallest item into position.
Use SortCompare to evaluate the effectiveness of doing so. Note : It is often possible to
avoid an index-out-of-bounds test in this way—the element that enables the test to be
eliminated is known as a sentinel.
2.1.25 Insertion sort without exchanges. Develop an implementation of insertion sort
that moves larger elements to the right one position with one array access per entry,
rather than using exch(). Use SortCompare to evaluate the effectiveness of doing so.
2.1.26 Primitive types. Develop a version of insertion sort that sorts arrays of int
values and compare its performance with the implementation given in the text (which
sorts Integer values and implicitly uses autoboxing and auto-unboxing to convert).
2.1.27 Shellsort is subquadratic. Use SortCompare to compare shellsort with insertion
sort and selection sort on your computer. Use array sizes that are increasing powers of
2, starting at 128.
2.1.28 Equal keys. Formulate and validate hypotheses about the running time of in-
sertion sort and selection sort for arrays that contain just two key values, assuming that
the values are equally likely to occur.
2.1.29 Shellsort increments. Run experiments to compare the increment sequence in
Algorithm 2.3 with the sequence 1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929,
16001, 36289, 64769, 146305, 260609 (which is formed by merging together the se-
quences 9·4k 9·2k 1 and 4k 3·2k 1). See Exercise 2.1.11.
2.1.30 Geometric increments. Run experiments to determine a value of t that leads to
the lowest running time of shellsort for random arrays for the increment sequence 1,
⎣t⎦, ⎣t 2⎦, ⎣t 3⎦, ⎣t 4⎦, . . . for N = 10 6. Give the values of t and the increment sequences for
the best three values that you find.
268 CHAPTER 2 ■ Sorting
EXPERIMENTS (continued)
The following exercises describe various clients for helping to evaluate sorting methods. They
are intended as starting points for helping to understand performance properties, using ran-
dom data. In all of them, use time(), as in SortCompare, so that you can get more accurate
results by specifying more trials in the second command-line argument. We refer back to these
exercises in later sections when evaluating more sophisticated methods.
2.1.31 Doubling test. Write a client that performs a doubling test for sort algorithms.
Start at N equal to 1000, and print N, the predicted number of seconds, the actual num-
ber of seconds, and the ratio as N doubles. Use your program to validate that insertion
sort and selection sort are quadratic for random inputs, and formulate and test a hy-
pothesis for shellsort.
2.1.32 Plot running times. Write a client that uses StdDraw to plot the average running
times of the algorithm for random inputs and various values of the array size. You may
add one or two more command-line arguments. Strive to design a useful tool.
2.1.33 Distribution. Write a client that enters into an infinite loop running sort() on
arrays of the size given as the third command-line argument, measures the time taken
for each run, and uses StdDraw to plot the average running times. A picture of the dis-
tribution of the running times should emerge.
2.1.34 Corner cases. Write a client that runs sort() on difficult or pathological cases
that might turn up in practical applications. Examples include arrays that are already
in order, arrays in reverse order, arrays where all keys are the same, arrays consisting of
only two distinct values, and arrays of size 0 or 1.
2.1.35 Nonuniform distributions. Write a client that generates test data by randomly
ordering objects using other distributions than uniform, including the following:
■ Gaussian
■ Poisson
■ Geometric
■ Discrete (see Exercise 2.1.28 for a special case)
Develop and test hypotheses about the effect of such input on the performance of the
algorithms in this section.
2.1 ■ Elementary Sorts
269
2.1.36 Nonuniform data. Write a client that generates test data that is not uniform,
including the following:
■ Half the data is 0s, half 1s.
■ Half the data is 0s, half the remainder is 1s, half the remainder is 2s, and so forth.
■ Half the data is 0s, half random int values.
Develop and test hypotheses about the effect of such input on the performance of the
algorithms in this section.
2.1.37 Partially sorted. Write a client that generates partially sorted arrays, including
the following:
■ 95 percent sorted, last percent random values
■ All entries within 10 positions of their final place in the array
■ Sorted except for 5 percent of the entries randomly dispersed throughout the
array
Develop and test hypotheses about the effect of such input on the performance of the
algorithms in this section.
2.1.38 Various types of items. Write a client that generates arrays of items of various
types with random key values, including the following:
■ String key (at least ten characters), one double value
■ double key, ten String values (all at least ten characters)
■ int key, one int[20] value
Develop and test hypotheses about the effect of such input on the performance of the
algorithms in this section.