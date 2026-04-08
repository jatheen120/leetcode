class Solution {
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int n=nums.length;
        for(int i=0;i<queries.length;i++){
            int idx=queries[i][0];
            while(idx<=queries[i][1]){
               nums[idx] = (int)((long)nums[idx] * queries[i][3] % 1000000007);
                idx+=queries[i][2];
            }
        }
        int xor=0;
        for(int x:nums) {
            xor^=x;
        }
        return xor;
    }
}