import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    bodies = list()
    scores = list()

    for _ in range(N):
        bodies.append(tuple(map(int, sys.stdin.readline().strip().split())))

    for body in bodies:
        score = 0
        for i in range(N):
            if body[0] < bodies[i][0] and body[1] < bodies[i][1]:
                score += 1
        scores.append(score + 1)

    print(*scores)
