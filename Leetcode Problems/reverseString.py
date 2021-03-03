# Approach 1: simple Python function (not ideal for interviews)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse()

# Approach 2: Traversing to mid and swapping elements from left and right
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        size = len(s)
        
        for i in range(size // 2):
            print(i)
            s[i], s[(size - 1) - i] = s[(size - 1) - i], s[i]
            
# Approach 3: list slicing (fastest)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s[:] = s[::-1]