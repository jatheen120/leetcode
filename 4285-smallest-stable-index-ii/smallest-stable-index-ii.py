class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        r=[0]*n
        r[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            r[i]=min(nums[i],r[i+1])
        maxi=0
        for i in range(n):
            maxi=max(maxi,nums[i])
            if maxi-r[i]<=k:
                return i
        return -1