package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class baekjoon_1449 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        List<Integer> holes = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            holes.add(Integer.valueOf(st.nextToken()));
        }

        Collections.sort(holes);

        int ans = 1;
        int start = holes.get(0) + L - 1;

        for (Integer hole : holes) {
            if (hole <= start)
                continue;
            start = hole + L - 1;
            ans += 1;
        }
        System.out.println(ans);
    }
}
