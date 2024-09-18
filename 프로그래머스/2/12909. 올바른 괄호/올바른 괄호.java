import java.util.*;
class Solution {
    boolean solution(String s) {

        Stack<Character> items = new Stack<>();
        for (char item : s.toCharArray()){
            if(item == '('){
                 items.push(item);
            } else {
                if (items.isEmpty()){
                    return false;
                }
                items.pop();
            }
   
        }
        return items.isEmpty();
    }
}