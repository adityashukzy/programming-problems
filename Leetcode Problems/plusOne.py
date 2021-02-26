class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        i = num = 0
        
        while i < len(digits):
            num += digits[idx] * (10**i)
            i += 1
            idx -= 1
        
        num += 1
        
        num = str(num)
        digits = []
        for dig in num:
            digits.append(int(dig))
        
        return digits