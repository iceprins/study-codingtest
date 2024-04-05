package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class baekjoon_2606 {
    static int[][] network;
    static boolean[] visited;
    static int computers;
    static int pairs;

    public static int bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        int count = 0;

        while (!q.isEmpty()) {
            int now = q.poll();

            for (int i = 0; i <= computers; i++) {
                if (network[now][i] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        computers = Integer.parseInt(br.readLine());
        pairs = Integer.parseInt(br.readLine());

        network = new int[computers + 1][computers + 1];
        visited = new boolean[computers + 1];

        for (int i = 0; i < pairs; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            network[a][b] = network[b][a] = 1;
        }
        br.close();

        System.out.println(bfs(1));
    }
}
