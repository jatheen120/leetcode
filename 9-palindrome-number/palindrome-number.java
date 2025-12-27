class Solution{
    public boolean isPalindrome(int n){
        if(n<0)return false;
        int a=n,b=0;
        while(n>0){
            b=b*10+n%10;
            n=n/10;
        }
        return a==b;
    }
}
