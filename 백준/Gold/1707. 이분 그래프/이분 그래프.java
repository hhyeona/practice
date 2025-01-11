import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<Integer>[] A; // 인접리스트
    static int[] check; //그래프 체크
    static boolean[] visited; // 방문표시
    static boolean IsEven; // 정답
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(bf.readLine());
        for(int t=0; t<TC; t++){
            String[] s = bf.readLine().split(" ");
            int N = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            // A를 초기화 해줌.
            A = new ArrayList[N+1];
            visited = new boolean[N+1];
            check = new int[N+1];
            IsEven = true;
            for(int i =1; i<=N; i++){
                A[i] = new ArrayList<Integer>();
            }
            // 엣지 데이터 저장 - 무방향
            for(int i=0; i<E; i++){
                s = bf.readLine().split(" ");
                int start = Integer.parseInt(s[0]);
                int end = Integer.parseInt(s[1]);
                A[start].add(end);
                A[end].add(start);
            }
            // 모든 노드에서 DFS 실행
            for(int i=1; i<=N; i++){
                if(IsEven){
                    DFS(i);
                } else {
                    break;
                }
            }
            if(IsEven) System.out.println("YES");
            else System.out.println("NO");
        }
    }

    private static void DFS(int node) {
        visited[node] = true;
        for(int i : A[node]){
            if(!visited[i]){
                // #바로 직전 노드와 다른 집합으로 분류
                check[i] = (check[node] + 1) % 2;  // 1 or 2
                DFS(i);
            }
            else if(check[node] == check[i]){
                    IsEven = false;
                    return;

                }
            }

        }
    }


