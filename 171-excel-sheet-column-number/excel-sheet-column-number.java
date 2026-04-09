class Solution {
    public int titleToNumber(String columnTitle) {
        char[] arr=columnTitle.toCharArray();
        int result=0;
        for(int i=0;i<arr.length;i++){
            int val=arr[i]-'A'+1;
            result=result*26+val;
        }

        return result;
    }
}