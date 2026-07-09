class Solution:
    def longestPalindrome(self, s: str) -> int:
        h={}
        
        for c in s:
            if c in h:
                h[c]+=1
            else:
                h[c]=1
        y=0
        count=0
        for x in h:
            if h[x]%2==0:
                count+=h[x]
            else:
                y+=1
                count+=h[x]-1
        if y>0:
            count+=1
        return count