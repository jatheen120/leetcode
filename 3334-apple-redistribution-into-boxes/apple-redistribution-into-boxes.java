class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        int sum = 0;
        for(int i=0;i<apple.length;i++){
            sum+=apple[i];
        }
        Arrays.sort(capacity);
        int c=0;
        for(int j = capacity.length - 1; j >= 0; j--){
            sum-=capacity[j];
            c++;
            if(sum<=0){
                return c;
            }
        }
        return c;
    }
}