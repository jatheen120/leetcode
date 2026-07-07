class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        x=0
        c=0
        for i in range(0,len(str(n))):
            d=n%10
            if d!=0:
                c+=1
                sum+=d
                x+=d*(10**(c-1))
            n=n//10
        
        return x*sum
