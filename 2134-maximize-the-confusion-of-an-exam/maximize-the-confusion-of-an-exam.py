class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ct=0
        cf=0
        maxi=0
        l=0
        for r in range(len(answerKey)):
            if answerKey[r]=='T':
                ct+=1
            else:
                cf+=1
            while(min(ct,cf)>k):
                if answerKey[l]=='T':
                    ct-=1
                else:
                    cf-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi 