import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int item : priorities){
            pq.add(item);
        }
        // System.out.println(pq);
        
        while(!pq.isEmpty()){
            for (int i=0; i<priorities.length; i++){
                if (priorities[i] == pq.peek()){
                    pq.poll();
                    answer ++;
                    if (i==location){
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}