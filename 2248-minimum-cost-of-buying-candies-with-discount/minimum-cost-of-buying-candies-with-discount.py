class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        took=0
        ans=0
        for i in range(len(cost)-1,-1,-1):
            if took==2:
                took=0
            else:
                took+=1
                ans+=cost[i]
        return ans