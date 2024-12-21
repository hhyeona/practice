import java.util.*;

// 연속된 숫자들의 합.
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

// 투포인터로 해결 O(n) - cnt가 1인 이유는 : 자기 자신 하나를 먼저 카운트.
        int start = 1;
        int end = 1;
        int sm = 1;
        int cnt = 1;
        // end 포인터가 n이 되면 종료.
        while (end != n) {
            if (sm == n) {
                cnt++;
                end++;
                sm += end;
            } else if (sm < n) {
                end++;
                sm += end;
            } else if (sm > n) {
                sm -= start-1;
                start++;

            }
        }
        System.out.println(cnt);
    }
}
