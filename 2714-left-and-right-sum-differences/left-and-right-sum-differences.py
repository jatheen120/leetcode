class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        nums1=[]
        nums2=[]
        l=0
        r=0
        for i in range(len(nums)):
            nums1.append(l)
            l+=nums[i]
        for i in range(len(nums)-1,-1,-1):
            nums2.append(r)
            r+=nums[i]
        nums2.reverse()
        for i in range(len(nums)):
            nums[i]=abs(nums1[i]-nums2[i])
        return nums