class Solution {
    public int bestClosingTime(String customers) {
        int pen=0;
        for (char c : customers.toCharArray()) {
            if(c=='Y') pen++;
        }
        int minPen=pen;
        int b=0;
        int n=customers.length();

        for (int i=0;i<n;i++) {
            if (customers.charAt(i)=='Y')pen--;
            else pen++;

            if (pen<minPen) {
                minPen=pen;
                b=i+1;
            }
        }

        return b;
    }
}
