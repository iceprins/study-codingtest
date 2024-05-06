import sys
from collections import deque


def bfs():
    q = deque()
    q.append(1)

    while q:
        x = q.popleft()
        if x == 100:
            print(board[x])
            break
        for dice in range(1, 7):
            next_pos = x + dice
            if next_pos <= 100 and not visited[next_pos]:
                if next_pos in ladder.keys():
                    next_pos = ladder[next_pos]
                if next_pos in snake.keys():
                    next_pos = snake[next_pos]
                if not visited[next_pos]:
                    visited[next_pos] = True
                    board[next_pos] = board[x] + 1
                    q.append(next_pos)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().strip().split())
    ladder = dict()
    snake = dict()

    board = [0] * 101
    visited = [False] * 101

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        ladder[a] = b

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        snake[a] = b

    bfs()
