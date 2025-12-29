class Solution{
    public int lengthOfLongestSubstring(String s){
        int l=0,m=0;
        Set<Character>a=new HashSet<>();
        for(int r=0;r<s.length();r++){
            while(a.contains(s.charAt(r))){
                a.remove(s.charAt(l));
                l++;
            }
            a.add(s.charAt(r));
            m=Math.max(m,r-l+1);
        }
        return m;
    }
}