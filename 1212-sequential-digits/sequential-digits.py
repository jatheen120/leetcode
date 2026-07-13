class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        for l in range(2,10):
            for s in range(1,11-l):
                num=0
                digit=s
                for _ in range(l):
                    num=num*10+digit
                    digit+=1
                if low<=num<=high:
                    ans.append(num)
        return ans