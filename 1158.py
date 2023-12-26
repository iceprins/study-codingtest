if __name__ == '__main__':
    N, K = map(int, input().split(" "))

    people = list(range(1, N + 1))
    ans = list()

    idx = 0
    for _ in range(N):
        idx += (K - 1)
        if idx > len(people):
            idx %= len(people)
        ans.append(people[idx])
        people.remove(people[idx])

    print(str(ans).replace('[', '<').replace(']', '>'))