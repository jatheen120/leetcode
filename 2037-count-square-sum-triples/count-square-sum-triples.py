class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range (1,n+1):
            for b in range (1,n+1):
                s=a*a+b*b
                r=int(s**0.5)
                if r*r==s and r<=n:
                    
                    count+=1
        return count