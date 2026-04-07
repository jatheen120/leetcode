class Robot {
    int x=0,y=0;
    int width,height;
    String dir="East";
    int per;
    boolean moved = false;

    public Robot(int width, int height) {
        this.width=width;
        this.height=height;
        per=2*(width+height)-4;
    }

    public void step(int num) {
        num=num%per;
        if(num==0&(x!=0 || y!=0)) num=per;
        while (num>0) {
            if (dir.equals("East")) {
                if (x+1<width) {
                    x++;
                    num--;
                } else {
                    dir="North";
                }
            }
            else if (dir.equals("North")) {
                if (y+1<height) {
                    y++;
                    num--;
                } else {
                    dir="West";
                }
            }
            else if (dir.equals("West")) {
                if (x-1>=0) {
                    x--;
                    num--;
                } else {
                    dir="South";
                }
            }

            else {
                if (y - 1 >= 0) {
                    y--;
                    num--;
                }else{
                    dir="East";
                }
            }
        }
        moved=true;
        if (x == 0 && y == 0 && moved) {
            dir = "South";
        }
    }
    public int[] getPos() {
        return new int[]{x, y};
    }
    public String getDir() {
        return dir;
    }
}

/**
 * Your Robot object will be instantiated and called as such:
 * Robot obj = new Robot(width, height);
 * obj.step(num);
 * int[] param_2 = obj.getPos();
 * String param_3 = obj.getDir();
 */