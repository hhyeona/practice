import java.io.*;
import java.util.*;
// 절댓값 우선순위 큐.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        // 우선순위 큐 커스터마이징 1.절댓값이 작은 것들 2.그 중에 음수먼저
        PriorityQueue<Integer> pQ = new PriorityQueue<>((o1,o2)->{
            int frist_abs = Math.abs(o1);
            int second_abs = Math.abs(o2);
            // 절댓값이 같은 경우 음수 우선.
            if(frist_abs==second_abs){
                return o1 > o2 ? 1: -1;
            }
            return frist_abs - second_abs;  // 절댓값 작은 데이터 우선.
        });
        // 입력값 받기
        for(int i=0; i<N; i++){
            int tm = Integer.parseInt(bf.readLine());
            if(tm!=0){
                pQ.add(tm);
            } else {
                if(!pQ.isEmpty()){
                    System.out.println(pQ.poll());
                } else {
                    System.out.println(0);
                }
            }
        }


    }
}
