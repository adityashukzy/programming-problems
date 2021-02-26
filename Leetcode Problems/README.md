# Problem-Solution Guide

## Two Sum (easy)
We are provided an array of elements 'nums', and a variable 'target'. We have to traverse the list and find the pair of elements whose sum is equal to the target. We then have to return the indices of this pair in any order.

### Return
We are supposed to return the indices of the pair in a list (order does not matter).

### Sample Input
nums = [2,7,11,15], target = 9

### Sample Output
[0, 1] or [1, 0]

### Approach1
Language Used: Python3
We traverse through each element of the list. For each element, we again traverse the list in an inner loop and check if the sum of our element and another element adds up to the target. If so, we return the values of the iteration variables i and j in a list.

#### Efficiency
Worst-case Time Complexity: O(n^2)

Worst-case Space Complexity: O(1)



### Approach2
Language Used: Python3
We initialize a dictionary (or hash-table). The purpose of this hash table is to store the complement for each variable traversed so far. Basically, say we encounter a value '2' at the 1th index and our target is '9', then we store (9 - 2) = 7 and this index 1 as an entry {7: 1} in the dictionary. We traverse through the list and for each element check if it's complement is available in the dictionary's keys. If so, we pack the index of the current element and the value of the entry in the dictionary (which stores the original element's index) into a list, and return this list.

#### Efficiency
Worst-case Time Complexity: O(n)

Worst-case Space Complexity: O(n)


## Maximum Subarray (easy)
We are provided a list 'nums'. Our job is to find the contiguous subarray (with at least one element) which has the maximum sum and then return its sum.

### Return
Return the sum of the contigious subarray which has maximum sum.

### Sample Input
nums = [-2,1,-3,4,-1,2,1,-5,4]

### Sample Output
6 (because [4,-1,2,1])

### Approach
Language Used: Python3
Kadane's algorithm used. We traverse through the list once with two variables: max_so_far and max_ending_here. Initially, we assign max_so_far to the maximum element of the list (this is for the scenario where we may have all negative numbers. In that case, we want it to return the biggest of them), and we initialize max_ending_here to zero.

We traverse through the list and for each element, we check if the sum including that element is greater than the max sum we have so far. If so, max_so_far is updated. If adding the current element to max_so_far results in a negative number, then we reset max_ending_here to zero. The reason behind this is that none of the contiguous subarrays so far could be greater than max_so_far and not only that, but now we also have max_ending_here as negative. So moving ahead, we want to shave off this negative value that we've been dumped with and start anew from the next element.

#### Efficiency
Worst-case Time Complexity: O(n)

Worst-case Space Complexity: O(1)