class Solution {
    public int dayOfYear(String date) {
        String[] parts=date.split("-");
        int y=Integer.parseInt(parts[0]);
        int m=Integer.parseInt(parts[1]);
        int day=Integer.parseInt(parts[2]);
        int[] d={31,28,31,30,31,30,31,31,30,31,30,31};
        if((y%4==0&&y%100!=0)||y%400==0){
            d[1]=29;
        }
        int total=0;
        for(int i=0;i<m-1;i++){
            total+=d[i];
        }
        total+=day;
        return total;
    }
}