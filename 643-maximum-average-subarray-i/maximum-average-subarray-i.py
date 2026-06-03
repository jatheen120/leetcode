class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        l=0
        ans=0
        maxi=float('-inf')
        for r in range(n):
            ans+=nums[r]
            if r-l+1>k:
                ans-=nums[l]
                l+=1
            if r-l+1==k:
                maxi=max(maxi,ans/k)
        return maxi