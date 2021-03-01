## Simple Approach: supposedly O(n^2) but runs pretty fast
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        
        for val in set(nums):
            if nums.count(val) > max_count:
                max_count = nums.count(val)
                max_val = val
        
        return max_val

## DAC Approach: supposedly O(n.log n) but runs quite slow
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def recursiveMajority(low, high):
            if low == high:
                return nums[low]
            
            mid = (low + high) // 2
            left = recursiveMajority(low, mid)
            right = recursiveMajority(mid+1, high)
            
            if left == right:
                return left
            
            left_count = sum(1 for i in range(low, high+1) if nums[i] == left)
            right_count = sum(1 for i in range(low, high+1) if nums[i] == right)
            
            if left_count > right_count:
                return left
            else:
                return right
        
        return recursiveMajority(0, len(nums) - 1)
