import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String sNum = sc.next(); // String으로 받는데, 입력값의 N이 100 범위라 int와 long으로 못 받음.
        char[] cNum = sNum.toCharArray(); // 따라서, 단어 하나씩으로 바꿔줌. 
        
        int sum = 0;
        for(int i = 0; i < N; i++){
            // 아스키 코드로 -48하면 숫자가 됨. 따라서 문자열 0을 빼주거나 -48 하면 숫자로 변환 가능.
            sum += cNum[i] - '0';            
        }
       System.out.println(sum);
    }
}