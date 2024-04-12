package codingTest;

import java.io.*;
import java.util.*;

public class baekjoon_1325 {
    static List<List<Integer>> arr;
    static boolean[] visited;
    static int[] ans;

    public static void dfs(int start) {
        visited[start] = true;

        for (Integer i : arr.get(start)) {
            if (visited[i])
                continue;
            ans[i]++;
            dfs(i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        arr = new ArrayList<>();
        visited = new boolean[N + 1];
        ans = new int[N + 1];

        for (int i = 0; i < N + 1; i++) {
            arr.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr.get(a).add(b);
        }

        for (int i = 1; i < N + 1; i++) {
            visited = new boolean[N + 1];
            dfs(i);
        }

        int maxVal = -1;

        for (int num : ans) {
            maxVal = Math.max(maxVal, num);
        }

        for (int i = 1; i < N + 1; i++) {
            if (ans[i] == maxVal)
                bw.write(i + " ");
        }

        bw.flush();
        br.close();
    }
}
