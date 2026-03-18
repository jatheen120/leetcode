class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = 0
        for part in p.split('*'):
            if part == "":
                continue
            j = s.find(part, i)
            if j == -1:
                return False
            i = j + len(part)
        return True