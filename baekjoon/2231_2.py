if __name__ == '__main__':
    N = int(input())

    ans = 0

    for num in range(1, N + 1):
        if num + sum(list(map(int, str(num)))) == N:
            ans = num
            break

    print(ans)
