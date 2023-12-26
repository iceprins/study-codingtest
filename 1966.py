import sys

if __name__ == '__main__':
    testcase = int(sys.stdin.readline().strip())

    for _ in range(testcase):
        N, M = map(int, sys.stdin.readline().strip().split(" "))
        waiting = list()
        priority = list(map(int, sys.stdin.readline().strip().split(" ")))

        for i in range(N):
            waiting.append((i, priority[i]))

        cnt = 1
        while True:
            if waiting[0][1] == max(waiting, key=lambda x:x[1])[1]:
                if waiting[0][0] == M:
                    print(cnt)
                    break
                waiting.pop(0)
                cnt += 1
                continue
            tmp = waiting.pop(0)
            waiting.append(tmp)