class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix=[]
        maxi=0
        for i in nums:
            maxi=max(i,maxi)
            prefix.append(gcd(i,maxi))
        prefix.sort()
        a=0
        n=len(prefix)
        for i in range(n//2):
            a+=gcd(prefix[i],prefix[n-i-1])
        return a