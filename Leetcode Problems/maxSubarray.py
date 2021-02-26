# Kadane's Algorithm => traversing through loop once so T.C.: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = max(nums)
        max_ending_here = 0
        
        for i, val in enumerate(nums):
            max_ending_here += val
            
            if max_ending_here < 0:
                max_ending_here = 0
            elif max_ending_here > max_so_far:
                max_so_far = max_ending_here
        
        return max_so_far