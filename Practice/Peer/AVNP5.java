package Practice.Peer;

import java.io.*;
import java.util.Arrays;

class SegmentTree {
    int[] st;
    int size;

    char[] s;
    int n;

    final static String vowels = "aeiou";

    public SegmentTree(char[] s) {
        this.s = s;
        this.n = s.length;

        int height = (int) Math.ceil(Math.log(n)/Math.log(2));
        size = 2 * (int) Math.pow(2, height) - 1;

        st = new int[size];
    }

    public int getMid(int s, int e) {
        return s + (e - s) / 2;
    }

    public void update(int stStart, int stEnd, int stIndex, int index, int value) {
        if(index < stStart || index > stEnd) {
            return;
        }
        if(stStart == stEnd) {
            st[stIndex] += value;
        }
        else {
            int mid = getMid(stStart, stEnd);

            if(index >= stStart && index <= mid) {
                update(stStart, mid, 2 * stIndex + 1, index, value);
            }
            else {
                update(mid + 1, stEnd, 2 * stIndex + 2, index, value);
            }

            st[stIndex] = st[2 * stIndex + 1] + st[2 * stIndex + 2];
        }
    }

    public void update(int index, char c) {
        boolean isExistingVowel = vowels.indexOf(s[index]) >= 0;
        boolean isIncomingVowel = vowels.indexOf(c) >= 0;
        s[index] = c;

        if((isExistingVowel && !isIncomingVowel) || (!isExistingVowel && isIncomingVowel)) {
            update(0, n - 1, 0, index, isIncomingVowel ? 1 : -1);
        }
    }

    public int query(int qs, int qe, int stStart, int stEnd, int index) {
        if(stStart > stEnd)
            return 0;

        if(qs > stEnd || qe < stStart)
            return 0;

        if(qs <= stStart && qe >= stEnd)
            return st[index];

        int mid = getMid(stStart, stEnd);

        return query(qs, qe, stStart, mid, 2 * index + 1)
                + query(qs, qe, mid + 1, stEnd, 2 * index + 2);
    }

    public int query(int l, int r) {
        return query(l, r, 0, n - 1, 0);
    }

    public int construct(int stStart, int stEnd, int stIndex) {
        if(stStart == stEnd) {
            st[stIndex] = vowels.indexOf(s[stStart]) >= 0 ? 1: 0;
            return st[stIndex];
        }

        int mid = getMid(stStart, stEnd);
        int l = construct(stStart, mid, 2 * stIndex + 1);
        int r = construct(mid + 1, stEnd, 2 * stIndex + 2);

        st[stIndex] = l + r;

        return st[stIndex];
    }

    public void construct() {
        construct(0, n - 1, 0);
    }

    @Override
    public String toString() {
        return Arrays.toString(st);
    }
}

public class AVNP5 {
    public static void main(String[] args) throws IOException {
        int t, q;
        String s;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pr = new PrintWriter(System.out);

        t = Integer.parseInt(br.readLine());

        while(t-- > 0) {
            s = br.readLine();

            SegmentTree segmentTree = new SegmentTree(s.toCharArray());
            segmentTree.construct();

            q = Integer.parseInt(br.readLine());

            String[] input;

            for(int i = 0; i < q; i ++) {
                input = br.readLine().split("\\s+");

                if(input[0].equals("F")) {
                    pr.println(segmentTree.query(Integer.parseInt(input[1]) - 1, Integer.parseInt(input[2]) - 1));
                }
                else {
                    segmentTree.update(Integer.parseInt(input[1]) - 1, input[2].charAt(0));
                }
            }
        }
        pr.close();
    }
}
