class Solution {
    public int closestTarget(String[] words,String target,int start){
        int n=words.length,min=Integer.MAX_VALUE;
        for(int i=0;i<n;i++){
            if(words[i].equals(target)){
                int d=Math.abs(i-start);
                int dist;
                if(d<n-d)dist=d;
                else dist=n-d;
                if(dist<min)min=dist;
            }
        }
        if(min==Integer.MAX_VALUE)return -1;
        return min;
    }
}