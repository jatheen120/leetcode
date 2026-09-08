class Solution:
    def countCommas(self, n: int) -> int:
        l=len(str(n))
        if l<=3:
            return 0
        m=1000
        while(n>=m):
            ans=n-m+1
            m=m*1000
        return ans
