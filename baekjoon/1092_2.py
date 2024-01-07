import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    weight_limit = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    box_weight = list(map(int, sys.stdin.readline().strip().split()))

    weight_limit.sort(reverse=True)
    box_weight.sort(reverse=True)

    cnt = 0

    if box_weight[0] > weight_limit[0]:
        cnt = -1
    else:
        while box_weight:
            cnt += 1
            for limit in weight_limit:
                if box_weight and limit < box_weight[-1]:
                    continue
                for weight in box_weight:
                    if weight <= limit:
                        box_weight.remove(weight)
                        break

    print(cnt)