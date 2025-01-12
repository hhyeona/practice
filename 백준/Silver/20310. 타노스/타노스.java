import java.io.*;
import java.util.*;
// 새로운 문자열을 만드는 것!! - 사전 순으로 빠르게
// (반대 개념) 제거 해야하는 1을 앞에서부터, 0을 뒤에서부터 탐색함.
// -> for문 한 번의 탐색으로 가능 0(n)
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String S = bf.readLine();
        // 0과 1의 수
        int cntZero = S.length() - S.replace("0","").length();
        int cntOne = S.length() - S.replace("1","").length();
        //제거해야 할 수
        int removeZero = cntZero / 2;
        int removeOne = cntOne / 2;
        // 문자열을 추가하면서 생기는 가비지 컬렉터를 줄이기 위해 변경가능한 문자열을 만들어 줌. - StringBuilder
        StringBuilder result = new StringBuilder();
        // 앞에서부터 1 제거.
        for(char c : S.toCharArray()){
            if(c=='1' && removeOne>0){
                removeOne--;
            } else {
                result.append(c);
            }
        }
        // 뒤에서 부터 0 제거 후, reverse 해서 출력.
        String tm = result.toString();
        result = new StringBuilder();
        for(int i=tm.length()-1; i>=0; i--){
            char c = tm.charAt(i);
            if(c=='0'&&removeZero >0){
                removeZero--;
            } else{
                result.append(c);
            }
        }
        System.out.println(result.reverse());
    }
}