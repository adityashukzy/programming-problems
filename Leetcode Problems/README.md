# Problem-Solution Guide

## 1. Two Sum (easy)
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


## 2. Maximum Subarray (easy)
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

## 3. Majority Element (easy)
We are provided a list 'nums'. Our job is to find the majority element. The majority element is the one which appears in the list more than [n/2] times.

### Return
Return the majority sum.

### Sample Input
nums = [2,2,1,1,1,2,2]

### Sample Output
2

### Approach 1
Language Used: Python3
Simple approach. I make a set of the list to find all the unique elements. I traverse through this set, and for each I find the count using the .count() method. For each unique element, if its count is greater than the current max, it is assigned as the new max. Finally, the value is returned for which the count is max (i.e. the final value once the loop is over.)

#### Efficiency
Worst-case Time Complexity: O(n^2)

Worst-case Space Complexity: O(n/2 + 1) = O(n) (will have a set which may at max have (n/2 + 1) unique elments.)

### Approach 2
Language Used: Python3
Divide and conquer. Divide list into two down the middle. Keep dividing until we are left with only one element in each subarray and then return that. At each phase of combining results, if the left and right subarray have same majority element, then great: this value is returned as majority for the particular combined subarray of those 2.
If they do not agree, then for the total subarray (that those 2 form), the count of each of their returned values is measured, and whichever is greater is returned.

#### Efficiency
Worst-case Time Complexity: O(n . log n) (supposedly faster than Approach 1 but giving slow results in Leetcode)

Worst-case Space Complexity: O(log n) (arrays are not passed at each recursion; only indices. However, the recursive calls build up in the stack and since we are dividing the array into two at each point, the number of calls will be log n.)
