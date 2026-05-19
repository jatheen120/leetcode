class Solution {
    public int getCommon(int[] nums1, int[] nums2) {
        for (int i=0;i<nums1.length;i++){
            int j=0;
            while(j<nums2.length && nums2[j]<=nums1[i]){
                if (nums2[j]==nums1[i]) return nums1[i];
                j++;
            }
        }
        return -1;
    }
}