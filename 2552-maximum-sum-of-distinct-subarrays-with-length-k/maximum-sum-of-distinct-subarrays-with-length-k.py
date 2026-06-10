class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        temp=0
        ans=0
        list1={}
        for r in range(len(nums)):
            temp+=nums[r]
            list1[nums[r]]=list1.get(nums[r],0)+1
            if(r-l+1>k):
                temp-=nums[l]
                list1[nums[l]]-=1
                if list1[nums[l]]==0:
                    del list1[nums[l]]
                l+=1
            if r-l+1==k and len(list1)==k:
                ans=max(ans,temp)
        return ans
