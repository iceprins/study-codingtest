import sys
from collections import deque

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        p = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        arr = deque(sys.stdin.readline().strip()[1:-1].split(","))
        flag = 0

        for ch in p:
            if ch == "R":
                flag += 1
            elif ch == "D":
                if n == 0:
                    print("error")
                    break
                else:
                    if flag % 2 == 1:
                        arr.pop()
                    else:
                        arr.popleft()
                n -= 1

        else:
            if flag % 2 == 1:
                arr.reverse()
            print("[" + ",".join(arr) + "]")
