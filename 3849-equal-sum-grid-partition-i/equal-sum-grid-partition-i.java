class Solution {
    public boolean canPartitionGrid(int[][] grid) {
        int rows=grid.length;
        int cols=grid[0].length;

        long total=0;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                total+=grid[i][j];
            }
        }
        long sum=0;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                sum+=grid[i][j];
            }
            if(sum*2==total) return true;
        }
        
        sum=0;
        for(int j=0;j<cols-1;j++){
            for(int i=0;i<rows;i++){
                sum+=grid[i][j];
            }
            if(sum*2==total) return true;
        }

        return false;
    }
}