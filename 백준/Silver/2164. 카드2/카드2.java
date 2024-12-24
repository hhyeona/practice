import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // queue 선언.
        Queue<Integer> myQueue = new LinkedList<>();
        for(int i=1; i<=n; i++){
            myQueue.add(i);
        }
        // myQueue 크기가 1이면 탈출.
        while (myQueue.size() > 1){
            // 맨위 카드 버리기
            myQueue.poll();
            // 그 다음 카드 추가.
            myQueue.add(myQueue.poll());
        }
        System.out.println(myQueue.poll());
    }

}
