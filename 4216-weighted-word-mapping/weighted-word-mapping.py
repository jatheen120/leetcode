class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""

        for word in words:
            s=0

            for ch in word:
                s+=weights[ord(ch)-ord('a')]

            ans+=chr(ord('z')-(s%26))

        return ans