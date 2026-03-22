class Solution {

    public boolean findRotation(int[][] mat, int[][] target) {
        for (int i = 0; i < 4; i++) {
            if (same(mat, target)) return true;
            rotate(mat);
        }
        return false;
    }

    private boolean same(int[][] a, int[][] b) {
        int n = a.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (a[i][j] != b[i][j]) return false;
            }
        }
        return true;
    }

    private void rotate(int[][] a) {
        int n = a.length;

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int x = a[i][j];
                a[i][j] = a[j][i];
                a[j][i] = x;
            }
        }

        for (int i = 0; i < n; i++) {
            int l = 0, r = n - 1;
            while (l < r) {
                int x = a[i][l];
                a[i][l] = a[i][r];
                a[i][r] = x;
                l++;
                r--;
            }
        }
    }
}