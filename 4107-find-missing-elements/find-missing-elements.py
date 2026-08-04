class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        c=[]
        for i in range (a,b):
            if i not in nums:
                c.append(i)
                
        return c
