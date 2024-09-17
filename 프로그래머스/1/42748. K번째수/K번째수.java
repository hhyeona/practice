import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int index = 0;
        for (int[] command : commands){
            int s = command[0] -1 ;
            int e = command[1];
            int k = command[2] -1 ;
            
            int[] tm = Arrays.copyOfRange(array,s,e);
            Arrays.sort(tm);
            answer[index++] = tm[k];
        }
        
        return answer;
    }
}