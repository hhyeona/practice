import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
// 데이터 10만개 나올 수 있으니까. for문으로 하나씩 계산하는 게 아니라. 합 배열을 구한 후, 구간 합을 계산. 2-3 이면 3-1 해주면 됨.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        // 옆으로 숫자가 길게 나오면 보통 토큰 하나로 쓸 수 있도록 String으로 입력 받음. (StringTokenizer)
        StringTokenizer  st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        // 0을 제외하고 입력 받을 것임.
        long[] smLst = new long[n+1];
        st = new StringTokenizer(bf.readLine());
        for(int i=1; i<=n; i++){
            int tm = Integer.parseInt(st.nextToken());
            smLst[i] = smLst[i-1] + tm;
        }
        for(int j = 0; j < m; j++){
            st = new StringTokenizer(bf.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(smLst[e]-smLst[s-1]);
        }
    }
}
