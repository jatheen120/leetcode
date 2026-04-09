class Solution {
    public int minOperations(int[] nums, int k) {
        int sum=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
        }
        if(sum<k) return sum;
        if(sum>k) return sum%k;
        if(sum==k) return 0;
        return k;
    }
}