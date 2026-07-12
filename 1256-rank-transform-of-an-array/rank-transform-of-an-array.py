class Solution(object):
    def arrayRankTransform(self, arr):
        a = arr[:]  
        a.sort()
        h={}
        b=[]
        c=0
        for i in a:
            c+=1
            if i not in h:
                h[i]=c
            else:
                c-=1
        for j in arr:
            b.append(h[j])
        return b