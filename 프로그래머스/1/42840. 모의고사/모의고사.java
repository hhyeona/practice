import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] person1 = {1,2,3,4,5};
        int[] person2 = {2,1,2,3,2,4,2,5};
        int[] person3 = {3,3,1,1,2,2,4,4,5,5,};
        List<Integer> score = new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        score.add(0);
        score.add(0);
        score.add(0);
        for (int i=0; i<answers.length; i++){
            if (answers[i] == person1[i%5]){
                score.set(0,score.get(0)+1);
            } if (answers[i] == person2[i%8]){
                score.set(1,score.get(1)+1);
            } if (answers[i] == person3[i%10]){
                score.set(2,score.get(2) +1);
            }
        }
        int mx = Collections.max(score);
        
        for(int j=0; j<score.size(); j++){
            if (mx == score.get(j)){
                ans.add(j+1);
            }
        }
        
               
        return ans.stream().mapToInt(i->i).toArray();
    }
}