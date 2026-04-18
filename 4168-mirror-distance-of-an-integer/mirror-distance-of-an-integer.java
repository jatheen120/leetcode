class Solution {
    public int rev(int x){
            int r=0;
        while(x>0) {
            int d=x%10;
            r=r*10+d;
            x=x/10;
        }
        return r;}
        
    public int mirrorDistance(int n) {
        return Math.abs(n-rev(n));
    }
}