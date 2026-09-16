class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x=rec1[0]
        y=rec1[2]
        x1=rec2[0]
        y1=rec2[2]

        l=rec1[1]
        m=rec1[3]
        l1=rec2[1]
        m1=rec2[3]

        if y <= x1 or y1 <= x or m <= l1 or m1 <= l:
            return False
        return True