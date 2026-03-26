class Solution {
    public int maximumGap(int[] nums) {
        Arrays.sort(nums);
        int n=nums.length;
        int maxi=0;
        for(int i=0;i<n-1;i++){
            maxi=Math.max(maxi,nums[i+1]-nums[i]);
        }
        return maxi;
    }
}