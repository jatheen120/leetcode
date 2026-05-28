class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ins=0
        ans=0
        for i in range(len(cost)-1,-1,-1):
            if ins==2:
                ins=0
            else:
                ins+=1
                ans+=cost[i]
        return ans