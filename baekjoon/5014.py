from collections import deque


def bfs(pos, v):
    queue = deque()
    queue.append(pos)
    v[pos] = 1
    while queue:
        now = queue.popleft()
        for new_pos in (now + up, now - down):
            if new_pos < 1 or new_pos > total:
                continue
            if v[new_pos] == 0:
                v[new_pos] = v[now] + 1
                queue.append(new_pos)


if __name__ == '__main__':
    total, current, dest, up, down = map(int, input().strip().split())
    visited = [0] * (total + 1)

    bfs(current, visited)

    if visited[dest] == 0:
        print("use the stairs")
    else:
        print(visited[dest] - 1)
