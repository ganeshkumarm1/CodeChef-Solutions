package Practice.Peer;

import java.util.*;

class ZACKHAN {
    public static int gcd(int a, int b) {
        if(a == 0) {
            return b;
        }

        return gcd(b % a, a);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        while (t -- > 0) {
            int l = sc.nextInt();
            int r = sc.nextInt();
            System.out.println(gcd(l, r));
        }

    }
}
