import java.util.*;

public class Main {
    public static void main(String[] args){
        /*
//        입력값 받기
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] lst = new int[n];
        for(int i = 0; i< n; i++){
            lst[i] = sc.nextInt();
        }
//  max값 찾기
        Arrays.sort(lst);
        int mx = lst[n-1];
        //수정해서 더하기
        float sm = 0;
        for(int num: lst) {
            float tm = ((float) num / mx) * 100;
            sm += tm;
        }
        // 평균내기.
        float ans = sm/n;
        System.out.println(ans);

         */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] lst = new int[n];
        for(int i = 0; i< n; i++){
            lst[i] = sc.nextInt();
        }
        Arrays.sort(lst);
        int mx = lst[n-1];
        int sm = 0;
//        (a+b+c)*100/M/n 으로 공식 단순화.
        for(int num:lst){
            sm += num;
        }
        float ans = (float) sm*100/mx/n;
        System.out.println(ans);
    }
}
