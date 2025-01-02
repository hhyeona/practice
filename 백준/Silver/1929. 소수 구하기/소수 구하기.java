import java.util.Scanner;

public class Main {
    //에라토스테네스의 체 방식.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] lst = new int[M+1];
        for(int i=2; i<=M; i++){
            lst[i] = i;
        }
        // 1은 소수가 아님. 제곱긊까지만 해줌.
        int sqrtM = (int)Math.sqrt(M);
        for( int i=2; i<=sqrtM; i++){
            // 소수가 아니면 넘어감 - 0으로 표시.
            if(lst[i]==0) continue;
            // 소수의 배수 값을 M까지 반복.
            for(int j=i+i; j<=M; j=j+i){
                lst[j] = 0;
            }
        }
        for(int i=N; i<=M; i++){
            if(lst[i]!=0){
                System.out.println(lst[i]);
            }
        }
    }
}
