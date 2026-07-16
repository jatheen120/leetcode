class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        t=0

        lmax=0
        rmax=0

        start=0
        end=n-1
        while(start<end):
            lmax=max(lmax,height[start])
            rmax=max(rmax,height[end])

            if(lmax<rmax):
                t+=lmax-height[start]
                start+=1
            else:
                t+=rmax-height[end]
                end-=1
        return t