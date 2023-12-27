import sys

if __name__ == '__main__':
    crane = int(sys.stdin.readline().strip())
    weight_limit = list(map(int, sys.stdin.readline().strip().split()))
    box = int(sys.stdin.readline().strip())
    box_weight = list(map(int, sys.stdin.readline().strip().split()))

    weight_limit.sort(reverse=True)
    box_weight.sort(reverse=True)

    if box_weight[0] > weight_limit[0]:
        print(-1)
    else:
        box_idx, crane_idx, time = 0, 0, 0
        while box_weight:
            if box_weight[box_idx] <= weight_limit[crane_idx]:
                box_weight.pop(box_idx)
                crane_idx += 1
                box_idx = 0
            else:
                box_idx += 1

            if crane_idx == crane or box_idx == len(box_weight):
                time += 1
                box_idx = 0
                crane_idx = 0

        print(time)