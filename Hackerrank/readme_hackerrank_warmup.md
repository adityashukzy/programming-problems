# Problem-Solution Guide

## Sales by Match
We are provided an array of numbers representing socks of different colors (each value denotes a separate color sock). Our task is to find how many pairs there are. The logic here is that two array items of the same value are the same color and hence part of a pair.

### Return
We are supposed to return the number of pairs.

### Sample Input
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

### Sample Output
3

### Approach
Language Used: Python3

I make a set out of the provided list so that I have a list of the unique elements (i.e. all the colors). Then I traverse through this set, and for each color, I find the corresponding number of socks. Finally, this number is divided by 2 and the decimal part is discarded by typecasting the float to an integer.

One iteration of the outer loop gives us the number of pairs for one color; the entire loop does this for each color and sums all the individual counts to get us the final count of all pairs.
