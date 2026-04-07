class Robot{
    int x=0,y=0;
    int width,height;
    String d="East";
    int per;
    boolean m=false;

    public Robot(int width,int height){
        this.width=width;
        this.height=height;
        per=2*(width+height)-4;
    }

    public void step(int num){
        num=num%per;
        if(num==0&(x!=0||y!=0))num=per;

        while(num>0){
            if(d.equals("East")){
                if(x+1<width){
                    x++;
                    num--;
                }else{
                    d="North";
                }
            }

            else if(d.equals("North")){
                if(y+1<height){
                    y++;
                    num--;
                }else{
                    d="West";
                }
            }

            else if(d.equals("West")){
                if(x-1>=0){
                    x--;
                    num--;
                }else{
                    d="South";
                }
            }

            else{
                if(y-1>=0){
                    y--;
                    num--;
                }else{
                    d="East";
                }
            }
        }

        m=true;

        if(x==0&&y==0&&m){
            d="South";
        }
    }

    public int[] getPos(){
        return new int[]{x,y};
    }

    public String getDir(){
        return d;
    }
}