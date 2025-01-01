import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i=0; i<N; i++){
            A[i] = Integer.parseInt(st.nextToken());
        }
        //A 배열 정렬.
        Arrays.sort(A);
        // 입력값 하나씩 이분탐색
        int M = Integer.parseInt(bf.readLine());
        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<M; i++){
            boolean find = false;
            int target = Integer.parseInt(st.nextToken());
            int start = 0;
            int end = A.length -1;
            while(start <= end){
                int mid = (start+end)/2;
                int mid_value = A[mid];
                if(mid_value > target){
                    end = mid - 1;
                } else if(mid_value < target){
                    start = mid+1;
                } else {
                    find = true;
                    break;
                }
            }
            if(find) System.out.println(1);
            else System.out.println(0);
        }

    }

}
