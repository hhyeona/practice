import java.io.*;
import java.util.*;

public class Main {
    // substring으로 배열 하나씩 숫자로 변환. substring(a, b) a부터 b-1까지.
    // 선택정렬 - 내림차순
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String st = sc.nextLine();
        int n = st.length();
        int[] lst = new int[n];
        // 하나씩 숫자로 변환.
        for(int i=0; i<n; i++){
            lst[i] = Integer.parseInt(st.substring(i,i+1));
        }
        // 선택 정렬
        for(int i=0; i<n; i++){
            int mx = i; // 맨 앞의 index로 max index 세팅.
            for(int j=i+1; j<n; j++){ // i 번째 이후 더 큰 index를 max index로 업데이트 == max 값 찾기.
                if(lst[j] > lst[mx]){
                    mx = j;
                }
            }
            // max index 값 찾았으면 swap
            if(lst[i] < lst[mx]){
                int tm = lst[i];
                lst[i] = lst[mx];
                lst[mx] = tm;
            }

        }
        // 한줄로 출력 ln 빼줌.
        for(int k=0; k<n; k++){
            System.out.print(lst[k]);
        }
    }
}
