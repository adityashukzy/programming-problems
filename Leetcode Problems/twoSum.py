## Approach 1: Brute-force; two-loops
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
					

## Approach 2: Hash-table with {(target - val): val's index}
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        indices = []
        
        for i, val in enumerate(nums):
            complement = target - val
            
            if val in hashTable.keys():
                indices.extend([hashTable[val], i])
            else:
                hashTable[complement] = i
        
        return indices