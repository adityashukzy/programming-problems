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
