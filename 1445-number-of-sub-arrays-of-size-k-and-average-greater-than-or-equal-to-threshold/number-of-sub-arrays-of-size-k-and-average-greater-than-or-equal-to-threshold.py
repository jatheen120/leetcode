class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        t=0
        l=0
        n=len(arr)
        for r in range(n):
            t+=arr[r]

            if(r-l==k):
                t=t-arr[l]
                l+=1
            if(r-l+1==k):
                if(t/k>=threshold):
                    c+=1
        return c


            

