class Solution {
    public int minMirrorPairDistance(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        int min=Integer.MAX_VALUE;

        for(int i=0;i<nums.length;i++){
            int rev=r(nums[i]);

            if(map.containsKey(nums[i])){
                min=Math.min(min,i-map.get(nums[i]));
            }

            map.put(rev,i);
        }

        if(min==Integer.MAX_VALUE){
            return -1;
        }else{
            return min;
        }
    }

    private int r(int x){
        int rev=0;
        while(x>0){
            rev=rev*10+(x%10);
            x/=10;
        }
        return rev;
    }
}