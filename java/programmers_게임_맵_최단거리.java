package codingTest;

import java.util.LinkedList;
import java.util.Queue;

public class programmers_게임_맵_최단거리 {
    public int solution(int[][] maps) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        int row = maps.length;
        int column = maps[0].length;

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0});
        maps[0][0] += 1;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            if (now[0] == row - 1 && now[1] == column - 1)
                break;

            for (int i = 0; i < 4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];

                if (nx < 0 || nx > row - 1 || ny < 0 || ny > column - 1 || maps[nx][ny] == 0)
                    continue;

                if (maps[nx][ny] == 1) {
                    maps[nx][ny] = maps[now[0]][now[1]] + 1;
                    q.add(new int[]{nx, ny});
                }
            }
        }

        if (maps[row - 1][column - 1] == 1)
            return -1;

        return maps[row - 1][column - 1] - 1;
    }
}
