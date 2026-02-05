class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n=nums.length;
        int[] nums1=new int[n];
        for(int i=0;i<n;i++){
            int r=nums[i];
            int x=i+r;
            x=x%n;
            if(x<0) x+=n;
            
            nums1[i]=nums[x];
        }
        return nums1;
    }
}