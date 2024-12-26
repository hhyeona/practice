import java.io.*;
import java.util.*;

public class Main {
    // BFS로 depth 간단하게 구함.
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};
    static boolean[][] visited;
    static int[][] A;
    static int N,M;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        A = new int[N][M];
        visited = new boolean[N][M];
        // 입력값 받기.2차원 배열.
        for(int i=0; i<N; i++){
            // 띄어쓰기 안됨. 한 줄 String으로 일단 그대로 받고 substring으로 나눔.
            st = new StringTokenizer(bf.readLine());
            String line = st.nextToken(); // ex) 101101011
            for(int j=0; j<M; j++){
                A[i][j] = Integer.parseInt(line.substring(j,j+1));
            }
        }
        //BFS 실행.
        BFS(0,0);
        System.out.println(A[N-1][M-1]);
    }

    private static void BFS(int i, int j) {
        Queue<int[]> que = new LinkedList<>(); //queue 선언.
        que.offer(new int[] {i,j}); // que에 i,j 추가.
        visited[i][j] = true;
        while(!que.isEmpty()){
            int[] now = que.poll();
            for(int k=0; k<4; k++){
                int ni = now[0] + dx[k];
                int nj = now[1] + dy[k];
                if(ni>=0 && nj>=0 && ni < N && nj < M){
                    if(A[ni][nj] != 0 && !visited[ni][nj]){
                        visited[ni][nj] = true;
                        A[ni][nj] = A[now[0]][now[1]] + 1; //depth 하나씩 증가.
                        que.add(new int[] {ni,nj});
                    }
                }
            }
        }
    }
}
