import sys
import re

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    p = re.compile('(100+1+|01)+')

    for _ in range(T):
        s = sys.stdin.readline().strip()
        if p.fullmatch(s):
            print("YES")
        else:
            print("NO")
