# Scenario
As a divide-and-conquer algorithm, Mergesort breaks the input array into subarrays and recursively sort them. When the sizes of sub-arrays are small, the overhead of many recursive calls makes the algorithm inefficient.

This problem can be remedied by choosing a small value of S as a threshold for the size of sub-arrays. When the size of a sub-array in a recursive call is less than or equal to the value of S, the algorithm will switch to Insertion sort, which is efficient for small input.

# Question
Implement the original version of Mergesort and the modified version of Mergesort. Compare their performances in the numbers of key comparisons and CPU times.

The value of S is to be empirically decided by trial and error.

# Our Application
- Input elements are integers and the goal is to sort input numbers in ascending order. Our application generates input data sets of random sizes, ranging from 1,000 to 1,000,000 random integers. Values of these integers range [1, n].
- Our application counts the number of key comparisons and CPU time taken by the program with the respective data sets, allowing comparison between the original and modified Mergesort algorithms.
- Our application will study how the different values of S will affect the performance of the modified algorithm.

# Built With
Python - Programming language
