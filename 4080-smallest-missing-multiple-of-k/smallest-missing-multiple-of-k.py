class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(k,k*200,k):
            if i not in  nums:
                return i
        return -1