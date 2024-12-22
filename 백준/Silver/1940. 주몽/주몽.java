// N개가 1만5천이라 정렬가능. - 투포인터
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        int m = Integer.parseInt(bf.readLine());
        long[] lst = new long[n];
        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i=0; i < n; i++){
            int tm = Integer.parseInt(st.nextToken());
            lst[i] = tm;
        }
        Arrays.sort(lst);
        int i = 0; int j = n-1;  int cnt=0;
        while (i<j){
            if(lst[i]+lst[j]<m){
                i++;
            } else if (lst[i]+lst[j]==m) {
                cnt++;
                i++;
                j--;
            } else if (lst[i]+lst[j] > m) {
                j--;
            }
        }
        System.out.println(cnt);
    }
}
