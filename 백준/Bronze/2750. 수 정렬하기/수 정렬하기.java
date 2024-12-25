import java.io.*;
import java.util.*;

public class Main {
    //Arrays.sort() 대신 버블정렬 해보기.
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] lst = new int[N];
        for(int i=0; i<N; i++){
            lst[i] = Integer.parseInt(bf.readLine());
        }
        // 버블정렬.
        for(int i=0; i<N-1; i++){ // i는 전체 횟수.
            for(int j = 0; j<N-1-i; j++){ // j는 앞 뒤 비교.
                if(lst[j]>lst[j+1]){
                    int temp = lst[j];
                    lst[j] = lst[j+1];
                    lst[j+1] = temp;
                }
            }
        }
    for(int i=0; i<N; i++){
        System.out.println(lst[i]);
    }
    }
}
