import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> day = new ArrayList<>();
        List<Integer> answer = new ArrayList<>();
        
        for (int i=0; i<progresses.length; i++){
            int tm = (int)Math.ceil((100 - progresses[i]) / (double) speeds[i]) ;
            day.add(tm);
        }
        // System.out.println(day);
      
        int tmm = day.get(0);
        int sum = 1;
        for (int j = 1; j < day.size(); j++){
            if (tmm < day.get(j)){
                answer.add(sum);
                sum = 1;
                tmm = day.get(j);
            } else {
                sum += 1;
            }
            
        }
//         마지막 sum 추가. (for문 다 끝난 후!!!)
        answer.add(sum);

        
        return answer.stream().mapToInt(i->i).toArray();
    }
}