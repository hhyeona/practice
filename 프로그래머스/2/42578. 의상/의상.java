import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> count = new HashMap<>();
        
        for (String[] item : clothes){
            String type = item[1];
   
            if (count.containsKey(type)){
                count.replace(type, count.get(type)+1);
            } else {
                count.put(type,1);
            }
                
        }
        
        // System.out.println(count.toString());
        for (String key : count.keySet()){
            answer *= count.get(key)+1;
        }
        
        
        return answer-1;
    }
}