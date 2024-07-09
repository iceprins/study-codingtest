def calculate(x):
    return (L // x) * (W // x) * (H // x)


def binary_search(lo, hi):
    for _ in range(100):
        mid = (lo + hi) / 2
        if calculate(mid) >= N:
            lo = mid
        elif calculate(mid) < N:
            hi = mid

    return hi


if __name__ == '__main__':
    N, L, W, H = map(int, input().split())

    start, end = 0, max(L, W, H)

    print(binary_search(start, end))
