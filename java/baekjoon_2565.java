package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_2565 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int lines = Integer.parseInt(br.readLine());

        List<int[]> pairs = new ArrayList<>();

        for (int i = 0; i < lines; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] pair = {Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())};
            pairs.add(pair);
        }

        Collections.sort(pairs, ((o1, o2) -> o1[0] - o2[0]));

        int[] dp = new int[lines];

        Arrays.fill(dp, 1);

        for (int i = 0; i < lines; i++) {
            for (int j = i + 1; j < lines; j++) {
                if (pairs.get(i)[1] < pairs.get(j)[1])
                    dp[j] = Math.max(dp[j], dp[i] + 1);
            }
        }
        System.out.println(lines - Arrays.stream(dp).max().orElse(0));
    }
}
