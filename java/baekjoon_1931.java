package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_1931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] plans = new int[N][2];
        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            plans[i][0] = Integer.parseInt(st.nextToken());
            plans[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(plans, (o1, o2) -> {

            if (o1[1] == o2[1]) {
                return o1[0] - o2[0];
            }
            return o1[1] - o2[1];

        });

        int end = 0;
        int cnt = 0;

        for (int[] plan : plans) {
            if (plan[0] >= end) {
                end = plan[1];
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
