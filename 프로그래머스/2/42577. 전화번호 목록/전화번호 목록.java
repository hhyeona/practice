import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        HashMap<String,Integer> map = new HashMap<>();
        
        for (String phone_number : phone_book){
            map.put(phone_number,1);
        }
        
        // System.out.println(map.toString());
        
        for (String phone_number : phone_book){
            for (int i = 1; i<phone_number.length(); i++ ){
                if (map.containsKey(phone_number.substring(0,i)))
                    return false;
            }
        }
        
        
        return true;
    }
}