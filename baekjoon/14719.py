import sys

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().strip().split())
    blocks = list(map(int, sys.stdin.readline().strip().split()))

    result = 0
    for i in range(1, width - 1):
        left_max = max(blocks[:i])
        right_max = max(blocks[i+1:])

        std_max = min(left_max, right_max)

        if blocks[i] < std_max:
            result += std_max - blocks[i]

    print(result)