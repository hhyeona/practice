import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    // 전역변수
    static int[] myArr = new int[4]; // 현재 진행 상태를 넣을 초기값.
    static int[] checkArr = new int[4]; // {acgt}
    static int checkNum = 0; // 충족된 checkArr의 숫자만큼 올려줌. 4가 되면 완성된 것 cnt 추가.
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int Result = 0; // 정답.
//        입력값.
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[] A; // 밑에서 .toCharArray로 배열 만들거라서 new char[] 안해줘도 됨. 
        A = bf.readLine().toCharArray();
        // 비밀 번호 숫자.
        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<4; i++){
            checkArr[i] = Integer.parseInt(st.nextToken());
            // 만약 0이라면? 비밀번호에 해당하지 않고 충족된 거니까.
            if(checkArr[i]==0){
                checkNum++;
            }
        }
        // 초기 A문자 배열 하나씩 현재 상태 배열에 들어와서 checkArr의 숫자 배열 하나씩 더해줌.
        for(int i=0; i<m; i++){
            Add(A[i]);
        }
        // checkNum한번 체크해줌.
        if(checkNum == 4) Result++;
        // 슬라이딩 윈도우
        for(int i=m; i<n; i++){
            int j = i-m;
            Add(A[i]);
            Remove(A[j]);
            if(checkNum == 4) Result++;
        }
        System.out.println(Result);
        bf.close();
    }
    // Remove 함수.
    private static void Remove(char c) {
        switch (c){
            case 'A':
                if(myArr[0] == checkArr[0]) checkNum--;
                myArr[0]--;
                break;
            case 'C':
                if(myArr[1] == checkArr[1]) checkNum--;
                myArr[1]--;
                break;
            case 'G':
                if(myArr[2] == checkArr[2]) checkNum--;
                myArr[2]--;
                break;
            case 'T':
                if(myArr[3] == checkArr[3]) checkNum--;
                myArr[3]--;
                break;
        }
    }

    // Add함수.
    private static void Add(char c) {
        switch (c){
            case 'A':
                myArr[0]++;
                if(myArr[0] == checkArr[0]) checkNum++;
                break;
            case 'C':
                myArr[1]++;
                if(myArr[1] == checkArr[1]) checkNum++;
                break;
            case 'G':
                myArr[2]++;
                if(myArr[2] == checkArr[2]) checkNum++;
                break;
            case 'T':
                myArr[3]++;
                if(myArr[3] == checkArr[3]) checkNum++;
                break;
        }
    }
}
