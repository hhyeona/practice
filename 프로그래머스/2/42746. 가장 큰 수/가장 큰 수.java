import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String[] arr = new String[numbers.length];
        int index = 0;
        
        for (int num : numbers){
            arr[index++] = String.valueOf(num);
        }
        
        Arrays.sort(arr, (s1,s2) -> (s2+s1).compareTo(s1+s2));
        
        if(arr[0].equals("0")){
            return "0";
        }
        
        StringBuilder answer = new StringBuilder();
        
        for(String item : arr){
            answer.append(item);
        }
        
        return answer.toString();
    }
}