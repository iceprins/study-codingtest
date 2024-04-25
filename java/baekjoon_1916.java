package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class baekjoon_1916 {
    static int N, M, depart, arrival;
    static List<List<BusInfo>> city;
    static boolean[] check;
    static int[] dist;

    static class BusInfo implements Comparable<BusInfo> {
        int end;
        int weight;

        public BusInfo(int end, int weight) {
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(BusInfo o) {
            return weight - o.weight;
        }
    }

    public static int dijkstra(int start) {
        PriorityQueue<BusInfo> q = new PriorityQueue<>();
        q.add(new BusInfo(start, 0));
        dist[start] = 0;

        while (!q.isEmpty()) {
            BusInfo now = q.poll();
            int nextArrival = now.end;

            if (!check[nextArrival]) {
                check[nextArrival] = true;

                for (BusInfo busInfo : city.get(nextArrival)) {
                    if (!check[busInfo.end] && dist[busInfo.end] > dist[nextArrival] + busInfo.weight) {
                        dist[busInfo.end] = dist[nextArrival] + busInfo.weight;
                        q.add(new BusInfo(busInfo.end, dist[busInfo.end]));
                    }
                }
            }
        }
        return dist[arrival];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());

        city = new ArrayList<>();
        check = new boolean[N + 1];
        dist = new int[N + 1];

        Arrays.fill(dist, Integer.MAX_VALUE);

        for (int i = 0; i <= N; i++) {
            city.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            city.get(a).add(new BusInfo(b, c));
        }

        st = new StringTokenizer(br.readLine());
        depart = Integer.parseInt(st.nextToken());
        arrival = Integer.parseInt(st.nextToken());

        System.out.println(dijkstra(depart));

        br.close();
    }
}
