class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        mini = nums.index(min(nums))
        maxi = nums.index(max(nums))

        left = min(mini, maxi)
        right = max(mini, maxi)

        return min(
            right + 1,          # remove from left
            n - left,           # remove from right
            left + 1 + n - right # remove both sides
        )