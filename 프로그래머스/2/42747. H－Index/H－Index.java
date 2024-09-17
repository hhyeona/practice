import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        // Arrays.sort(배열, Collections.reverseOrder()); Integer가능. int 안됨.
       
        // System.out.println(Arrays.toString(citations));
        
        int len = citations.length;
        
        for ( int i =0; i <= len-1; i++ ){
            int h= len-i;
            
            if (citations[i] >= h){
                answer = h;
                    break;
            }
        }
        
        
        return answer;
    }
}