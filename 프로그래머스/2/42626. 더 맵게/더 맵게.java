import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {

        int cnt = 0;
        PriorityQueue<Integer> pri = new PriorityQueue<>();
        
        for (int i=0; i<scoville.length; i++){
            pri.add(scoville[i]);
            
        }
        
        while (pri.size() > 1){
            if (pri.peek() >= K){
                return cnt;
            }
            
            int hot1 = pri.poll();
            int hot2 = pri.poll();
            
            pri.add(hot1+hot2*2);
            cnt ++;
        }
        
        if (pri.peek() > K){
            return cnt;
        }    
        
        return -1;
    }
}