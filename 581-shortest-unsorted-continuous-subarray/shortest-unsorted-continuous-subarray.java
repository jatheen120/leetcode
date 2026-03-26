class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n=nums.length;
        int[] bin=new int[n];
        for(int i=0;i<nums.length;i++){
            bin[i]=nums[i];
        }
        Arrays.sort(bin);
        int start=-1,end=-1;
        for(int i = 0; i < n; i++){
            if(nums[i] != bin[i]){
                start = i;
                break;
            }
        }
        if(start==-1) return 0; 
        for(int i=n-1;i>=0;i--){
            if(nums[i]!=bin[i]){
                end=i;
                break;
            }
        }
        return end-start+1;
    }
}