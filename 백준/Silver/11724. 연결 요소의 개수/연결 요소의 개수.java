import java.io.*;
import java.util.*;

public class Main {
    static boolean visited[];
    static ArrayList<Integer>[] A; // 노드리스트 선언.
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        visited = new boolean[n+1];
        A = new ArrayList[n+1];
        // 노드리스트의 인접리스트 초기화.
        for(int i=1; i<n+1; i++){
            A[i] = new ArrayList<Integer>();
        }
        // 인접리스트에 데이터 저장 - 무방향
        for(int i=0; i<m; i++){
            st = new StringTokenizer(bf.readLine());
            int s = Integer.parseInt(st.nextToken()); // 시작점
            int e = Integer.parseInt(st.nextToken()); // 종료점
            A[s].add(e);
            A[e].add(s);
        }
        // dfs 보내기.
        int cnt = 0;
        for(int i=1; i<n+1; i++){
            // 방문하지 않은 노드면 cnt 늘려주고 dfs 보냄.
            if(!visited[i]){
                cnt++;
                DFS(i);
            }
        }
        System.out.println(cnt);
    }
    //DFS 함수.
    private static void DFS(int i) {
        //종료 조건 : visited배열에 이미 있으면 종료.
        if(visited[i]){
            return;
        }
        visited[i] = true;
        // 인접 리스트 배열 안의 요소들 돌면서 방문 체크 - 안했다면 재귀함수
        for(int v: A[i]){
            if(!visited[v]){
                DFS(v);
            }
        }
    }
}
