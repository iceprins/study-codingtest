package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_15683 {
    static int N, M;
    static int ans = Integer.MAX_VALUE;
    static int[][] office;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][][] mode = {
            {},
            {{0}, {1}, {2}, {3}},
            {{0, 2}, {1, 3}},
            {{0, 1}, {1, 2}, {2, 3}, {0, 3}},
            {{0, 1, 2}, {1, 2, 3}, {0, 2, 3}, {0, 1, 3}},
            {{0, 1, 2, 3}}
    };
    static List<cctvInfo> cctv = new ArrayList<>();

    static class cctvInfo {
        int type;
        int x;
        int y;

        public cctvInfo(int type, int x, int y) {
            this.type = type;
            this.x = x;
            this.y = y;
        }
    }

    public static void dfs(int depth, int[][] before) {
        if (depth == cctv.size()) {
            int cnt = countBlindSpot(before);
            ans = Math.min(ans, cnt);
            return;
        }

        int cctvType = cctv.get(depth).type;
        int x = cctv.get(depth).x;
        int y = cctv.get(depth).y;

        int[][] backup = new int[N][M];

        for (int i = 0; i < N; i++) {
            backup[i] = before[i].clone();
        }

        for (int i = 0; i < mode[cctvType].length; i++) {
            fill(backup, mode[cctvType][i], x, y);
            dfs(depth + 1, backup);

            for (int j = 0; j < N; j++) {
                backup[j] = before[j].clone();
            }
        }
    }

    public static void fill(int[][] board, int[] direction, int x, int y) {
        for (int i = 0; i < direction.length; i++) {
            int nx = x;
            int ny = y;
            while (true) {
                nx += dx[direction[i]];
                ny += dy[direction[i]];
                if (nx < 0 || nx > N - 1 || ny < 0 || ny > M - 1)
                    break;
                if (board[nx][ny] == 6)
                    break;
                if (board[nx][ny] == 0)
                    board[nx][ny] = -1;
            }
        }
    }

    public static int countBlindSpot(int[][] map) {
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0)
                    cnt += 1;
            }
        }
        return cnt;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        office = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (num >= 1 && num <= 5) {
                    cctv.add(new cctvInfo(num, i, j));
                }
                office[i][j] = num;
            }
        }

        dfs(0, office);

        System.out.println(ans);
    }
}
