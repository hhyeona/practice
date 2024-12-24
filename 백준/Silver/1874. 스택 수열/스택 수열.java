import java.util.Scanner;
import java.util.Stack;

public class Main{
    public static void main(String[] args) {
        // 입력값.
        Scanner sc  = new Scanner(System.in);
        int n  = sc.nextInt();
        int A[]  = new int[n];
        for(int i=0; i<n; i++){
            A[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        int num = 1; //start 1부터 하나씩 넣음.
        boolean result = true; // No이면 false flag 표시.

        StringBuffer bf = new StringBuffer(); // String 배열 넣을 것임.
        for(int i = 0; i<A.length; i++){
            int su = A[i];  // 입력 숫자 꺼냄.
            // if 숫자크기 만큼 스택에 넣고 해당 숫자를 꺼냄.
            if(su >= num){
                while (su>=num){
                   stack.push(num++);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            }
            // 스택 맨 위의 값(ju)이 입력 값보다 크면 NO/ 같으면 POP
             else {
                int ju = stack.pop();
                if(ju > su){
                    System.out.println("NO");
                    result = false;
                    break;
                } else {
                    bf.append("-\n");
                }
            }
        }
        //flag가 true면 bf 배열 출력.
        if(result) System.out.println(bf);
    }
}
