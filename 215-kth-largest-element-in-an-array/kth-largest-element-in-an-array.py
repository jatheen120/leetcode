class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        y=sorted(nums)
        return y[n-k]