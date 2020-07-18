package Practice.Peer;

import java.util.Arrays;
import java.util.Scanner;

class FenwickTree {
    private int[] BIT;
    private int[] input;

    public FenwickTree(int[] array) {
        this.BIT = new int[array.length];
        this.input = array;
    }

    public void build() {
        int n = input.length;
        BIT = new int[n + 1];

        for(int i = 0; i <= n; i ++) {
            BIT[i] = 0;
        }

        for(int i = 0; i < n; i ++) {
            int value = input[i];
            input[i] = 0;
            update(i, value);
        }
    }

    public int getSum(int index) {
        index += 1;
        int sum = 0;

        while (index > 0) {
            sum += BIT[index];
            index = getParent(index);
        }

        return sum;
    }

    public int getSum(int l, int r) {
        return getSum(r) - getSum(l - 1);
    }

    public int getNext(int index) {
        return index + (index & -index);
    }

    public int getParent(int index) {
        return index - (index & -index);
    }

    public void update(int index, int value) {
        input[index] += value;
        index += 1;


        while(index < BIT.length) {
            BIT[index] += value;
            index = getNext(index);
        }
    }

    public String toString() {
        return "Input: " + Arrays.toString(input) + "\n" + "BIT: [" + Arrays.toString(BIT).substring(4);
    }
}

class ECJN208 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] array = new int[n];

        for(int i = 0; i < n; i ++) {
            array[i] = sc.nextInt();
        }

        FenwickTree fenwickTree = new FenwickTree(array);
        fenwickTree.build();
        int q =sc.nextInt();

        int type, a, b;

        StringBuilder s = new StringBuilder();
        for(int i = 0; i < q; i ++) {
            type = sc.nextInt();
            a = sc.nextInt();
            b = sc.nextInt();

            if(type == 0) {
                fenwickTree.update(a - 1, b);
            }
            else {
                int avg = (int) Math.ceil((double) fenwickTree.getSum(a - 1, b - 1)/(b - a + 1));
                s.append(avg).append('\n');
            }
        }

        System.out.println(s.toString().substring(0, s.toString().length() - 1));

    }
}
