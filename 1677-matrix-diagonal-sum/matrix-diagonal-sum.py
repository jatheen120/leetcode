class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        n=len(mat)
        print(n)
        for i in range(0,len(mat[0])):
            for j in range(0,len(mat[0])):
                if i==j:
                    s+=mat[i][j]
                if i+j==n-1:
                    s+=mat[i][j]
        if n%2!=0:
            s=s-mat[n//2][n//2]
        return s