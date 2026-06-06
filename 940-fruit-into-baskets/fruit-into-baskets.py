class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=0
        dic={}
        k=2
        for r in range(len(fruits)):
            val=fruits[r]
            if val in dic:
                dic[val]+=1
            else:
                dic[val]=1
            while (len(dic)>k):
                lval=fruits[l]
                dic[lval]-=1
                if dic[lval]==0:
                    dic.pop(lval)
                l+=1
            ans=max(ans,r-l+1)
        return ans
