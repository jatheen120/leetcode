class Solution:
    def maxProduct(self, n: int) -> int:

        maxi1=0
        maxi2=0

        while(n):
            d=n%10
            if (d>maxi1):
                maxi2=maxi1
                maxi1=d
            elif(d>maxi2):
                maxi2=d
            n=n//10
        return maxi1*maxi2
            
