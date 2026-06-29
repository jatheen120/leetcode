class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        c=0
        for x in patterns:
            if x in word:
                c+=1
        return c