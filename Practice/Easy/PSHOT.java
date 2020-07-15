import java.util.Scanner;

class PSHOT {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long t = sc.nextLong();

        while(t-- > 0) {
            long n = sc.nextLong();

            String s = sc.next();

            long scoreA = 0, scoreB = 0;
            long leftA = n, leftB = n;
            
            int i;
            for(i = 1; i <= 2 * n; i ++) {
                char goal = s.charAt(i - 1);

                if((i & 1) == 1) {
                    scoreA += goal == '1' ? 1 : 0;
                    leftA --;
                }
                else {
                    scoreB += goal == '1' ? 1 : 0;
                    leftB --;
                }

                if(scoreA > scoreB + leftB || scoreB > scoreA + leftA || (scoreA == scoreB && i == 2 * n)) {
                    break;
                }
            }
            
            System.out.println(i);
        }
    }
}