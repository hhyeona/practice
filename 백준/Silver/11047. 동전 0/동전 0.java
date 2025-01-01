import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] lst = new int[N];
        for( int i=0; i<N; i++){
           lst[i] = sc.nextInt();
        }
        int cnt =0;
        // 그리디 알고리즘 - 큰 동전 먼저 사용.
        for(int j=N-1; j>=0; j--){
            if(K>=lst[j]){
            cnt += K/lst[j];
            K = K%lst[j];
            }
        }
        System.out.println(cnt);
    }
}
