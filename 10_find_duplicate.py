import collections
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return nums[0]
        d=collections.defaultdict(int)
        for i in nums:
            d[i]+=1
            
     
        for i in nums:
            if d[i]>1:
                return i
            