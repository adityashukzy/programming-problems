class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        my_list = []
        
        while i < len(nums):
            if nums[i] not in my_list:
                my_list.append(nums[i])
            else:
                nums.pop(i)
                i -= 1
            
            i += 1
        
        my_list.clear()
        return len(nums)