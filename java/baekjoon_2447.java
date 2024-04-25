package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class baekjoon_2447 {
    static int N;
    static String[][] arr;

    public static void makeStars(int x, int y, int n) {
        if (n == 1) {
            arr[x][y] = "*";
            return;
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i != 1 || j != 1) {
                    makeStars(x + i * (n / 3), y + j * (n / 3), n / 3);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        arr = new String[N][N];

        for (int i = 0; i < N; i++) {
            Arrays.fill(arr[i], " ");
        }

        makeStars(0, 0, N);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(arr[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
