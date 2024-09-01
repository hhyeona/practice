import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int N = nums.length / 2;
        Set<Integer> set = new HashSet<Integer>();
        
        for(int i=0; i < nums.length; i++){
            if (!set.contains(nums[i])) 
                set.add(nums[i]);
            
        }
        int answer = set.size() < N ? set.size() : N;
        
        return answer;
    }
}