from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = Counter(nums)  
        for i in nums:
            if a[i]==1:
                return i
