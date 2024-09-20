class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int mx = 0;
        int mi = 0;
        
        for (int i=0; i<sizes.length; i++){
            if(sizes[i][0] > sizes[i][1]){
                mx = Math.max(mx,sizes[i][0]);
                mi = Math.max(mi,sizes[i][1]);
            } else {
                mx = Math.max(mx,sizes[i][1]);
                mi = Math.max(mi,sizes[i][0]);
            }
        }
        answer = mi * mx;
        
        return answer;
    }
}