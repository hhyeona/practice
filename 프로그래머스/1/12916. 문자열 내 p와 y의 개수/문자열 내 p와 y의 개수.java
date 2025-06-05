class Solution {
    boolean solution(String s) {
        boolean answer = true;
    
        int pCnt = 0;
        int yCnt = 0;
        
        char[] stList = s.toCharArray();
        for(char c:stList){
            if(c=='p' || c=='P'){
                pCnt+=1;
                }
            else if(c=='y'||c=='Y'){
                yCnt+=1;
            } 
        }

        if(pCnt!=yCnt) answer = false;
        return answer;
    }
}