import sys
from itertools import permutations


def game(line_ups):
    hitter_idx = 0
    score = 0
    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if inning[line_ups[hitter_idx]] == 0:
                out += 1
            elif inning[line_ups[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[line_ups[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inning[line_ups[hitter_idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif inning[line_ups[hitter_idx]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0

            hitter_idx = (hitter_idx + 1) % 9

    return score


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    innings = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    max_score = 0

    for line_ups in permutations(range(1, 9), 8):
        line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
        max_score = max(max_score, game(line_ups))

    print(max_score)
