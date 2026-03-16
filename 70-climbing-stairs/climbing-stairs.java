class Solution {
    int[] cache;
    public int climbStairs(int n) {
        if (cache == null)
            cache = new int[n + 1];
        
        if(n<=2)
            return n;

        if (cache[n] != 0)
            return cache[n];
        
        cache[n] = climbStairs(n - 1) + climbStairs(n - 2);
        return cache[n]; 
    }
}