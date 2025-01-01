import java.util.Scanner;

public class Main {
    static int ans = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ex = sc.nextLine();
        // - 기준으로 나눔.
        String[] str = ex.split("-");
        for(int i=0; i<str.length; i++){
            // +를 mySum 함수를 통해 더해줌.
            int tm = mySum(str[i]);
            if(i==0){
                ans += tm;
            } else {
                ans -= tm;
            }
        }
        System.out.println(ans);
    }

    private static int mySum(String s) {
        int sum = 0;
        // [] 하면 + 인식 잘 됨.
        String[] temp = s.split("[+]");
        for(int i=0; i< temp.length; i++){
            // 숫자로 변환 후 더함.
            sum+= Integer.parseInt(temp[i]);
        }
        return sum;
    }
}
