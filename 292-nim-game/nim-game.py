class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4==0:
            return False
        if n<=3 or n%3<=3:
            return True
        return False