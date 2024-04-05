package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_2667 {
    static int N;
    static int[][] complex;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static int bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        complex[x][y] = 0;
        int cnt = 0;

        while (!q.isEmpty()) {
            cnt++;
            int[] now = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                if (nx < 0 || nx > N - 1 || ny < 0 || ny > N - 1)
                    continue;
                if (complex[nx][ny] == 1) {
                    q.add(new int[]{nx, ny});
                    complex[nx][ny] = 0;
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        complex = new int[N][N];

        for (int i = 0; i < N; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < N; j++) {
                complex[i][j] = tmp.charAt(j) - '0';
            }
        }

        List<Integer> ans = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (complex[i][j] == 1)
                    ans.add(bfs(i, j));
            }
        }

        Collections.sort(ans);

        System.out.println(ans.size());

        for (Integer i : ans) {
            System.out.println(i);
        }
    }
}
