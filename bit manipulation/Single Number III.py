class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        a = 0
        for x in nums:
            a = a ^ x
        rb = a & -a
        a , b = 0 , 0
        for x in nums:
            if (x & rb) != 0:
                a = a ^ x
            else:
                b = b ^ x
            
        return [a, b]