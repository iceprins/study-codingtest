package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_1092 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        List<Integer> limits = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            limits.add(Integer.parseInt(st.nextToken()));
        }

        int M = Integer.parseInt(br.readLine());
        List<Integer> weights = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) {
            weights.add(Integer.parseInt(st.nextToken()));
        }

        limits.sort(Collections.reverseOrder());
        weights.sort(Collections.reverseOrder());

        int ans = 0;

        if (weights.get(0) > limits.get(0)) {
            System.out.println(-1);
            return;
        }

        while (!weights.isEmpty()) {
            int idx = 0;
            for (int i = 0; i < N; ) {
                if (idx == weights.size())
                    break;
                else if (limits.get(i) >= weights.get(idx)) {
                    weights.remove(idx);
                    i++;
                } else
                    idx++;
            }
            ans++;
        }
        System.out.println(ans);
    }
}
