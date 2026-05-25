class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        l=0
        ans=0
        dic={}
        for r in range(n):
            if s[r] in dic:
                dic[s[r]]+=1
            else:
                dic[s[r]]=1
            if(r-l==3):
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    dic.pop(s[l])

                l+=1
            
            if(len(dic)==3):
                ans+=1
            
        return ans