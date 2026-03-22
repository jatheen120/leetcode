class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(c.lower() for c in s if c.isalnum())
        return x == x[::-1]