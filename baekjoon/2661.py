def back(cnt):
    if not check(cnt):
        return -1
    if cnt == N:
        print(*result, sep='')
        return 1
    for i in range(1, 4):
        result.append(i)
        if back(cnt + 1) == 1:
            return 1
        result.pop()


def check(cnt):
    for i in range(cnt):
        slice_temp = result[i:]
        for j in range(1, len(slice_temp) // 2 + 1):
            if slice_temp[:j] == slice_temp[j:j * 2]:
                return False
    return True


if __name__ == '__main__':
    N = int(input())
    result = []

    back(0)
