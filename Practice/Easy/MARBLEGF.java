import java.util.*;
import java.io.*;

class MARBLEGF {
    static List<Long> binaryIndexTree;

    public static int getNext(int index) {
        return index + (index & -index);
    }

    public static int getParent(int index) {
        return index - (index & -index);
    }

    public static void update(int index, Long value) {
        index += 1;
        while (index < binaryIndexTree.size()) {
            binaryIndexTree.set(index, binaryIndexTree.get(index) + value);
            index = getNext(index);
        }
    }

    public static void build(List<Long> input) {
        int n = input.size();

        binaryIndexTree = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            binaryIndexTree.add(0L);
        }

        for (int i = 0; i < n; i++) {
            update(i, input.get(i));
        }
    }

    public static long getSum(int index) {
        long sum = 0L;
        index += 1;

        while (index > 0) {
            sum += binaryIndexTree.get(index);
            index = getParent(index);
        }

        return sum;
    }

    public static long getSum(int l, int r) {
        long lSum = getSum(l - 1);
        long rSum = getSum(r);

        return rSum - lSum;
    }

    public static void main(String[] args) {
        FastReader bu = new FastReader();
        StringBuilder sb = new StringBuilder();
        int n = bu.nextInt(), q = bu.nextInt();
        int i;
        long a[] = new long[n];
        List<Long> array = new ArrayList<>();

        for (i = 0; i < n; i++) {
            array.add(bu.nextLong());
        }

        build(array);

        while (q-- > 0) {
            int ch = bu.next().charAt(0);

            if (ch == 'G' || ch == 'T') {
                i = bu.nextInt();
                long val = bu.nextLong();
                if (ch == 'T')
                    val = -val;
                update(i, val);
                a[i] += val;
            } else {
                i = bu.nextInt();
                int j = bu.nextInt();
                long sum = getSum(i, j);
                sb.append(sum + "\n");
            }
        }
        System.out.print(sb);
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}