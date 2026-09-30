class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        base = 0
        count = {}

        for i in range(1, len(nums)):
            a = nums[i - 1]
            b = nums[i]

            if a == b:
                base += 1
            else:
                pair = tuple(sorted((a, b)))

                if pair not in count:
                    count[pair] = 0

                count[pair] += 1

        maximum = 0

        for value in count.values():
            maximum = max(maximum, value)

        return base+maximum